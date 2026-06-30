"""
第三课：分支 —— 根据条件决定走哪条路
"""

from datetime import datetime
from airflow.sdk import dag, task


@dag(
    dag_id="lesson_03_branch",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["lesson"],
)
def lesson_03_branch():

    @task
    def get_score():
        return 85  # 假设考试得了 85 分

    @task.branch
    def check_score(score):
        if score >= 60:
            return "pass_"  # 必须和下面的函数名一致
        else:
            return "fail"

    @task
    def pass_():
        print("Passed！")

    @task
    def fail():
        print("failed!")

    score = get_score()
    branch = check_score(score)
    branch >> [pass_(), fail()]


lesson_03_branch()

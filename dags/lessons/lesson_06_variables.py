"""
第六课：Variable —— 把配置从代码里分离出来
"""

from datetime import datetime
from airflow.sdk import dag, task
from airflow.models import Variable


@dag(
    dag_id="lesson_06_variables",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["lesson"],
)
def lesson_06_variables():

    @task
    def read_config():
        # 从 Airflow UI 里读取变量，不用写死在代码里
        env = Variable.get("environment", default_var="dev")
        threshold = Variable.get("score_threshold", default_var="60")

        print(f"当前环境：{env}")
        print(f"分数门槛：{threshold}")
        return int(threshold)

    @task
    def use_config(threshold):
        score = 75
        if score >= threshold:
            print(f"{score} 分，达到门槛 {threshold}，通过！")
        else:
            print(f"{score} 分，未达到门槛 {threshold}，未通过。")

    threshold = read_config()
    use_config(threshold)


lesson_06_variables()

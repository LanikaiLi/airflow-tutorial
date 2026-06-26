"""
第一课：你的第一个 DAG
运行后会执行一个任务，在日志里打印 Hello Airflow!
"""

from datetime import datetime

from airflow.decorators import dag, task


@dag(
    dag_id="lesson_01_hello",
    start_date=datetime(2024, 1, 1),
    schedule=None,  # 不自动定时跑，只在手动触发时运行
    catchup=False,  # 不补跑历史日期
    tags=["lesson"],
)
def lesson_01_hello():
    @task
    def say_hello():
        print("Hello Airflow!")
        return "done"

    say_hello()


lesson_01_hello()

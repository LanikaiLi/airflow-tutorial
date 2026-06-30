"""
第五课：失败重试（retry）
任务失败时，Airflow 自动重试几次再放弃
"""

from datetime import datetime, timedelta
from airflow.sdk import dag, task


@dag(
    dag_id="lesson_05_retry",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
    tags=["lesson"],
    default_args={
        "retries": 3,               # 失败后最多重试 3 次
        "retry_delay": timedelta(seconds=5),  # 每次重试间隔 5 秒
    },
)
def lesson_05_retry():

    @task
    def unstable_task():
        import random
        if random.random() < 0.7:   # 70% 概率失败
            raise Exception("模拟随机失败！")
        print("这次成功了！")

    unstable_task()


lesson_05_retry()

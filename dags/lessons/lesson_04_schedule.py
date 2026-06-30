"""
第四课：定时自动跑（schedule）
不用每次手动 Trigger，让 Airflow 按时间自动执行
"""

from datetime import datetime
from airflow.sdk import dag, task


@dag(
    dag_id="lesson_04_schedule",
    start_date=datetime(2024, 1, 1),
    #schedule="@daily",  # 每天自动跑一次
    schedule="0 9 * * *",  # cron expression for scheduling, 9am utc every day
    catchup=False,      # catchup only works when schedule is set, it means to run all the missed scheduled runs from start_date
    tags=["lesson"],
)
def lesson_04_schedule():

    @task
    def say_good_morning():
        print("早安！今天的每日任务开始了。")

    say_good_morning()


lesson_04_schedule()

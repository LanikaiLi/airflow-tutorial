"""
第二课：两个有顺序的 Task
先执行 step_one，完成后再执行 step_two
"""

from datetime import datetime

from airflow.decorators import dag, task


@dag(
    dag_id="lesson_02_sequence",
    start_date=datetime(2024, 1, 1),
    schedule=None, # 不自动定时跑，只在手动触发时运行
    catchup=False, # 不补跑历史日期
    tags=["lesson"],
)
def lesson_02_sequence():

    @task
    def step_one():
        print("第一步：开始处理数据")
        return "data from step one"

    @task
    def step_two(data):
        print(f"第二步：收到了 '{data}'，继续处理")
        print("全部完成！")

    # 箭头方向 = 执行顺序
    # step_one 的返回值，直接传给 step_two 当参数
    result = step_one()
    step_two(result)


lesson_02_sequence()

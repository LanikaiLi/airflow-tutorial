from airflow.decorators import dag, task
from datetime import datetime

@dag(
    dag_id="practice_01_sequence_bad_example",
    start_date=datetime(2024, 1, 1),
    schedule=None, # 不自动定时跑，只在手动触发时运行
    catchup=False, # 不补跑历史日期
    tags=["practice"],
)

def practice_01_sequence():
    @task
    def step_one():
        print("第一步：开始处理数据")
        return 10
    
    @task 
    def step_two(data):
        print(f"第二步：收到了 '{data}'，继续处理")
        return data * 2
    
    @task 
    def step_three(data):
        print(f"第三步：收到了 '{data}', 继续处理")
        print("最终结果是：", data)

    result = step_one()
    step_two(result)
    step_three(result)


practice_01_sequence()
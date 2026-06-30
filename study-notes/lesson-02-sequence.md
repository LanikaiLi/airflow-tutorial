# 第二课：两个有顺序的 Task

## 今天学一件事

**让两个 Task 按顺序执行，并且把第一步的结果传给第二步。**

---

## 核心概念

### Task 之间的顺序

Airflow 不会自动知道哪个先跑。你要在代码里**明确告诉它顺序**。

最简单的方式（TaskFlow 写法）：

```python
result = step_one()     # 先跑
step_two(result)        # 用 step_one 的返回值 → Airflow 知道它必须等前者完成
```

`step_one()` 的返回值直接当参数传给 `step_two()`，  
Airflow 看到这个依赖关系，就会**自动保证顺序**：先跑 step_one，再跑 step_two。

### Task 之间传数据

```python
@task
def step_one():
    return "data from step one"   # 返回一个值

@task
def step_two(data):               # 接收上一步的返回值
    print(data)
```

`step_one` 的返回值会被 Airflow 存起来，等 `step_two` 跑时再传进去。  
这个机制叫 **XCom**（cross-communication），现在不需要记这个词，知道「可以传值」就行。

---

## 代码

```python
@dag(...)
def lesson_02_sequence():

    @task
    def step_one():
        print("第一步")
        return "data from step one"

    @task
    def step_two(data):
        print(f"第二步：收到了 '{data}'")

    result = step_one()
    step_two(result)     # result 就是让 Airflow 知道顺序的关键

lesson_02_sequence()
```

---

## 在 UI 里会看到什么

Graph 视图里，两个方块之间会有一条箭头：

```
[step_one] → [step_two]
```

箭头方向 = 执行方向。

---

## 动手步骤

终端启动（如果还没启动）：

```bash
cd ~/airflow-tutorial
source py_env/bin/activate
export AIRFLOW_HOME="$PWD/airflow_home"
export AIRFLOW__CORE__DAGS_FOLDER="$PWD/dags"
export AIRFLOW__CORE__LOAD_EXAMPLES="False"
airflow standalone
```

浏览器打开 http://localhost:8080，找到 `lesson_02_sequence`：

1. 打开左侧开关（Unpause）
2. 点 **Trigger** 手动运行
3. 点进 DAG → 看 **Graph** 视图，确认有箭头
4. 点每个任务方块 → **Log**，看打印内容

---

## 检查自己学会了没有

- [ ] Graph 里看到两个方块，中间有箭头
- [ ] step_one 的 Log 有「第一步」
- [ ] step_two 的 Log 有「第二步：收到了 'data from step one'」
- [ ] 两个 task 都是绿色（成功）

---

## 第一课 vs 第二课

| | 第一课 | 第二课 |
|---|--------|--------|
| Task 数量 | 1 个 | 2 个，有顺序 |
| Task 之间传值 | 无 | step_one 传给 step_two |
| Graph 视图 | 一个方块 | 两个方块 + 箭头 |

---

## 下一课预告

第三课：用 **if/else** 控制 DAG 走哪条路（根据条件决定下一步）。

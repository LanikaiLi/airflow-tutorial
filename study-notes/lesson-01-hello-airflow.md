# 第一课：Airflow 是什么 + 跑第一个任务

## 今天只学一件事

**启动 Airflow，手动运行一个任务，在网页上看到它成功。**

---

## Airflow 是什么？（不用记术语）

想象你在管理一个**自动化任务清单**：

- 每天早上 8 点下载数据
- 然后清洗数据
- 最后发一封邮件报告

Airflow 就是帮你 **安排、运行、记录** 这些步骤的工具。

你写一份「任务清单」（代码），Airflow 按顺序或按时间帮你跑，并在网页上显示成功还是失败。

---

## 三个词（够用了）

| 词 | 大白话 |
|----|--------|
| **DAG** | 一份任务清单（一个 `.py` 文件通常就是一个 DAG） |
| **Task** | 清单里的一小步（比如「打印 Hello」） |
| **UI** | 网页界面，看任务跑得怎么样 |

---

## 项目里多了什么

```
dags/lesson_01_hello.py   ← 你写的任务清单（会提交 Git）
airflow_home/             ← Airflow 运行时数据（不提交 Git）
py_env/                   ← Python 环境（不提交 Git）
```

`dags/` 里的代码 = 你的业务逻辑  
`airflow_home/` = Airflow 自己的数据库、日志等

---

## 动手步骤

### 1. 打开终端，进入项目

```bash
cd ~/airflow-tutorial
source py_env/bin/activate
export AIRFLOW_HOME="$PWD/airflow_home"
export AIRFLOW__CORE__DAGS_FOLDER="$PWD/dags"
export AIRFLOW__CORE__LOAD_EXAMPLES="False"
```

最后两行说明：
- 告诉 Airflow：DAG 文件在项目的 `dags/` 文件夹
- 不加载官方示例，界面更干净

### 2. 启动 Airflow

```bash
airflow standalone
```

等终端出现类似 `Airflow is ready` 的提示。  
浏览器打开：**http://localhost:8080**

**登录账号（Airflow 3.x）：**

- 用户名：`admin`
- 密码：看文件 `airflow_home/simple_auth_manager_passwords.json.generated`

在终端查看：

```bash
cat ~/airflow-tutorial/airflow_home/simple_auth_manager_passwords.json.generated
```

你会看到类似 `{"admin": "随机密码"}`。密码是第一次启动时自动生成的。


### 3. 在网页上运行你的 DAG

1. 找到 **lesson_01_hello**
2. 点左侧开关，把 DAG **打开**（Unpause）
3. 右上角点 **Trigger**（手动触发）
4. 点 DAG 名字进入详情 → 点 **Graph** 或 **Grid**
5. 点任务方块 → **Log**，应该能看到 `Hello Airflow!`

### 4. 停止 Airflow

在运行 `airflow standalone` 的终端按 `Ctrl + C`。

---

## 代码在干什么（逐行理解）

```python
@dag(...)          # 定义一份任务清单
def lesson_01_hello():
    @task          # 清单里的第一步
    def say_hello():
        print("Hello Airflow!")
    say_hello()      # 把这一步加进清单

lesson_01_hello()  # 让 Airflow 识别这个 DAG
```

- `schedule=None` → 不会每天自动跑，只有你点 Trigger 才跑
- `catchup=False` → 不会把过去漏掉的日子全补跑一遍

---

## 检查自己学会了没有

- [ ] 能说出 DAG 和 Task 分别是什么
- [ ] 能启动 `airflow standalone` 并打开网页
- [ ] 能在 UI 里 Trigger `lesson_01_hello` 并看到成功
- [ ] 能在 Log 里看到 `Hello Airflow!`

---

## 下一课预告

第二课：一个 DAG 里放 **两个有顺序的任务**（先 A 后 B）。

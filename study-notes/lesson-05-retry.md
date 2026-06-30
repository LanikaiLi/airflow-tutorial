# 第五课：失败重试（retry）

## 为什么需要 retry

真实世界里任务失败很常见：
- 网络抖了一下，API 没响应
- 数据库短暂不可用
- 第三方服务超时

与其让整个 DAG 挂掉，不如**自动重试几次**，大多数短暂问题重试一下就过去了。

---

## 怎么配置

在 `@dag` 里加 `default_args`，对这个 DAG 里所有 task 生效：

```python
@dag(
    ...
    default_args={
        "retries": 3,                          # 失败后最多重试 3 次
        "retry_delay": timedelta(seconds=5),   # 每次重试间隔 5 秒
    },
)
```

也可以只给某一个 task 单独设置：

```python
@task(retries=2, retry_delay=timedelta(minutes=1))
def my_task():
    ...
```

---

## 在 UI 里看到的

task 方块颜色：
- **橙色**：正在重试
- **红色**：重试次数用完，彻底失败
- **绿色**：某次重试成功了

点进失败的 task → Log，每次重试都有记录，能看到每次失败的原因。

---

## `raise Exception` 是什么

```python
raise Exception("模拟随机失败！")
```

`raise` = 主动抛出一个错误，让 task 立刻失败。

Airflow 看到 task 抛出错误，就触发重试。真实场景里不需要你手动 raise，错误自然会发生（比如网络超时）。

---

## retry 不是万能的

retry 适合**短暂、偶发**的问题。如果是代码写错了、数据格式不对，重试多少次都没用，要去修代码。

---

## 下一课预告

第六课：用变量和连接（Variable & Connection）管理配置，不把密码写在代码里。

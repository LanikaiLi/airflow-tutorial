# 第三课：分支

## 今天学一件事

根据条件，让 DAG 走不同的路。

---

## 新概念：`@task.branch`

普通 `@task` 就是做一件事，做完继续往下。

`@task.branch` 是一个**岔路口**：它根据条件返回下一步要跑的 task 名字，Airflow 就跑那个，跳过其他的。

```python
@task.branch
def check_score(score):
    if score >= 60:
        return "pass_"   # 告诉 Airflow：去跑 pass_ 这个 task
    else:
        return "fail"    # 告诉 Airflow：去跑 fail 这个 task
```

返回值不是数字或字符串数据，而是**下一个 task 的名字**。

---

## 顺序怎么写

前两课用的是：

```python
result = step_one()
step_two(result)
```

分支用 `>>` 箭头：

```python
branch = check_score(score)
branch >> [pass_(), fail()]   # branch 之后可能走 pass_ 或 fail
```

`>>` 的意思是「然后」。`[pass_(), fail()]` 是两条可能的路，Airflow 只会跑 branch 返回的那个。

---

## 在 UI 里会看到什么

Graph 视图：

```
[get_score] → [check_score] → [pass_]
                            ↘ [fail]  ← 这个会是灰色（被跳过）
```

被跳过的 task 显示为灰色，不是失败，是「intentionally skipped」（故意跳过）。

---

## 顺便修掉 WARNING

之前的 WARNING：

```
airflow.decorators.dag is deprecated
```

原因是我们 import 的路径是旧版写法。Airflow 3.x 推荐：

```python
# 旧写法（会有 WARNING）
from airflow.decorators import dag, task

# 新写法（第三课开始用这个）
from airflow.sdk import dag, task
```

---

## 检查自己学会了没有

- [ ] 跑完后 Graph 里有分叉箭头
- [ ] `pass_` 是绿色，`fail` 是灰色（被跳过）
- [ ] `pass_` 的 Log 里有「恭喜，通过了！」
- [ ] 把 `get_score` 里的 85 改成 50，重新 Trigger，结果反过来

---

## 下一课预告

第四课：定时自动跑（`schedule`），让 DAG 不用手动 Trigger。

# 第四课：定时自动跑（schedule）

## 今天学一件事

让 DAG 按时间自动跑，不用每次手动 Trigger。

---

## `schedule` 可以填什么

### 预设值（最常用）

| 写法 | 意思 |
|------|------|
| `None` | 不自动跑，只能手动 Trigger |
| `"@once"` | 只自动跑一次 |
| `"@hourly"` | 每小时跑一次 |
| `"@daily"` | 每天跑一次（午夜） |
| `"@weekly"` | 每周跑一次 |
| `"@monthly"` | 每月跑一次 |

### Cron 表达式（更灵活）

```
"0 9 * * *"   每天早上 9 点
"0 9 * * 1"   每周一早上 9 点
"*/30 * * * *" 每 30 分钟
```

Cron 格式：`分 时 日 月 周`，`*` 表示「每个」。现在不用记，知道有这个就行。

---

## `start_date` 现在变重要了

前几课 `schedule=None`，`start_date` 没什么用。

有了 `schedule` 之后：

- Airflow 从 `start_date` 这天开始算，按 schedule 排定运行时间
- `catchup=False`：只从现在开始跑，过去的忽略
- `catchup=True`：从 `start_date` 到现在，把每一次漏掉的都补跑

**例子**：

```python
start_date = datetime(2024, 1, 1)
schedule = "@daily"
catchup = True   # 危险！
```

今天是 2026 年 6 月，Airflow 会发现从 2024-01-01 到现在漏了将近 900 次，全部排队补跑。

所以学习时**永远用 `catchup=False`**。

---

## 在 UI 里怎么看下次运行时间

DAG 列表页，每个 DAG 有一列 **Next Run**，显示下次自动运行的时间。

手动 Trigger 不受 schedule 影响，随时都可以点。

---

## 注意

`@daily` 实际是「UTC 时间午夜」触发，不是你本地时间的午夜。学习阶段不用在意，生产环境再考虑时区。

---

## 检查自己学会了没有

- [ ] DAG 列表里看到 `lesson_04_schedule` 的 **Next Run** 有时间显示
- [ ] 手动 Trigger 一次，任务成功
- [ ] 把 `schedule="@daily"` 改成 `schedule="@hourly"`，看 Next Run 时间变化

---

## 下一课预告

第五课：DAG 失败了怎么办——重试（retry）和失败通知。

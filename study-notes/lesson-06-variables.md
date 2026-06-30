# 第六课：Variable

## 问题：不要把配置写死在代码里

```python
# 不好：写死在代码里
threshold = 60
env = "production"
```

这样做的问题：
- 要改配置就得改代码、重新部署
- 密码、token 不能出现在代码里（会进 Git）

---

## Variable 是什么

Airflow 提供的一个**键值对存储**，保存在 Airflow 的数据库里。

在 UI 里管理，在代码里读取，**代码本身不包含具体的值**。

```python
from airflow.models import Variable

env = Variable.get("environment")           # 读取，不存在会报错
env = Variable.get("environment", default_var="dev")  # 有默认值，不存在不报错
```

---

## 怎么在 UI 里创建 Variable

1. 顶部菜单 → **Admin** → **Variables**
2. 点 **+** 新建
3. 填 Key 和 Value，保存

| Key | Value |
|-----|-------|
| `environment` | `production` |
| `score_threshold` | `80` |

---

## 代码里不改，UI 里改值，效果立刻不同

第一次跑：UI 里没有设变量 → 用 `default_var="dev"` 和 `"60"`

你在 UI 里加了 `environment=production`、`score_threshold=80` 之后再 Trigger → 代码读到新值，行为变了。

**代码没动，结果不同** —— 这就是 Variable 的价值。

---

## Connection 是什么（了解即可）

Connection 是 Variable 的升级版，专门用来存**数据库、API 等外部服务的连接信息**：

```
host: my-database.com
port: 5432
login: admin
password: ****
```

同样在 UI 里管理（Admin → Connections），代码里用 connection id 引用。

密码不进代码，不进 Git，安全。

真正连接数据库的时候再深入学，现在知道「有这个东西」就够了。

---

## Variable vs 写死在代码里

| | 写死在代码 | Variable |
|---|-----------|----------|
| 改配置 | 改代码 + 重新部署 | 在 UI 里改，立刻生效 |
| 密码安全 | 危险，进 Git | 安全，存在数据库 |
| 多环境（dev/prod） | 要维护多份代码 | 改一个变量值就切换 |

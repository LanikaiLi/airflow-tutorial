# Airflow 本地环境搭建 — 学习笔记

## 1. 两个文件夹，各管什么

| 文件夹 | 谁创建 | 存什么 |
|--------|--------|--------|
| `py_env/` | 你：`python -m venv py_env` | Python + 安装的包（Airflow 等） |
| `airflow_home/` | Airflow 第一次运行时自动创建 | 配置、数据库、日志、DAG 目录 |

- `py_env` = **软件**（程序装在哪）
- `airflow_home` = **数据**（程序跑起来产生的文件）

---

## 2. 为什么要虚拟环境（venv）

不同项目可能需要不同的 Python 版本和包版本。venv 给每个项目一个**独立小环境**，互不影响。

- 不污染系统 Python
- 搞坏了删文件夹重来即可
- 团队可以按同一份 `requirements.txt` 重建环境

**类比**：`py_env` ≈ Node 的 `node_modules`

---

## 3. 安装顺序（先有鸡再有蛋）

```
① Homebrew 装 Python 3.12     ← 系统 3.9 不够用，且不想动系统 Python
② python3.12 -m venv py_env   ← 给项目开独立环境
③ pip install -r requirements.txt  ← 往 venv 里装 Airflow
④ export AIRFLOW_HOME=...     ← 告诉 Airflow 数据放哪
⑤ airflow standalone          ← 启动
```

- **Homebrew**：在 macOS 上额外装软件（如 Python 3.12），不动系统自带的 3.9
- **activate 后**：终端里的 `python` / `pip` 指向 `py_env`，不是系统 Python

---

## 4. 为什么不把 py_env 提交 Git

`py_env` 体积大、和本机绑定、可以随时重建。Git 里存**配方**，不存**装好的环境**。

别人 clone 后自己执行：

```bash
python3.12 -m venv py_env
source py_env/bin/activate
pip install -r requirements.txt
```

---

## 5. requirements.txt 和 lock

| 概念 | 作用 | Node 类比 |
|------|------|-----------|
| 宽松依赖 | `pandas>=2.0`，装时选最新符合版 | `package.json` 里的 `^` |
| lock | `pandas==2.1.4`，每次装同一版本 | `package-lock.json` |
| constraint 文件 | Airflow 官方锁定的整套依赖版本 | 官方 curated lock |

本项目：

```txt
apache-airflow==3.2.0
--constraint https://.../constraints-3.2.0/constraints-3.12.txt
```

主包版本 + 官方 constraint = 可复现、稳定的安装。

---

## 6. AIRFLOW_HOME 是什么

```bash
export AIRFLOW_HOME="$PWD/airflow_home"
```

告诉 Airflow：**配置、数据库、日志放哪**。

- 不设 → 默认 `~/airflow`
- 设成项目里的 `airflow_home/` → 数据和项目在一起，更清晰

---

## 7. 日常命令速查

```bash
cd ~/airflow-tutorial
source py_env/bin/activate
export AIRFLOW_HOME="$PWD/airflow_home"
airflow standalone
```

浏览器打开 http://localhost:8080

---

## 8. 一句话总结

- **Homebrew Python**：提供 3.12 运行时
- **py_env**：这个项目专用的包环境
- **requirements.txt + constraint**：别人能复现的依赖配方
- **airflow_home**：Airflow 运行时的配置和数据
- **Git 提交代码和配方，不提交 py_env 和 airflow_home**

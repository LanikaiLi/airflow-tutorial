# Python 依赖管理 vs Node.js —— 对比笔记

## 核心类比（先建立直觉）

| Python（这个项目） | Node.js | 作用 |
|--------------------|---------|------|
| `py_env/` | `node_modules/` | 装依赖的本地文件夹，**不提交 Git** |
| `requirements.txt` | `package.json` | 声明「我需要什么包」 |
| `pip freeze > requirements.txt` | （接近 `package-lock.json`，但不完全是） | 把当前环境所有包版本写进文件 |
| `poetry.lock` / `uv.lock` | `package-lock.json` | **真正的 lock 文件** |
| Airflow 的 `--constraint ...txt` | 官方 curated lock | 官方测试过的完整版本组合 |

---

## 什么是 lock？为什么需要？

### 不 lock（宽松声明）

```txt
pandas>=2.0
requests
```

- 安装时 pip 选**当前满足条件的最新版**
- 你今天装 `pandas 2.1.0`，同事下个月装可能是 `2.3.0`
- **问题**：「我机器能跑，你那报错」

### lock（精确锁定）

```txt
pandas==2.1.4
numpy==1.26.4
requests==2.32.3
```

- 每次、每人装的是**完全相同的版本**
- **好处**：可复现，团队一致，部署稳定

---

## Node 是怎么分的

**`package.json`** — 声明意图（宽松）

```json
{
  "dependencies": {
    "lodash": "^4.17.0"
  }
}
```

`^4.17.0` 表示「4.x 里较新的都行」，**不是精确版本**。

**`package-lock.json`** — 精确记录（完整 lock）

- 记录 lodash 精确是 `4.17.21`
- 还记录 lodash 的依赖、依赖的依赖……**整棵依赖树都锁死**
- `npm install` 优先按 lock 装，大家一致

流程：`package.json`（我要什么）→ `npm install` → 生成 `package-lock.json`（实际装了什么）

---

## Python 是怎么分的

Python **没有一个全民统一的 lock 标准**，有几种做法：

| 做法 | 像 Node 的什么 | 说明 |
|------|----------------|------|
| `requirements.txt` 写 `pkg>=1.0` | `package.json` | 宽松，不保证一致 |
| `requirements.txt` 写 `pkg==1.2.3` | 部分 lock | 只锁你列出的包，子依赖可能仍然变 |
| `pip freeze > requirements.txt` | 接近 lock，但粗糙 | 把当前 venv 里所有包版本全导出 |
| `poetry.lock` / `uv.lock` | 真正的 `package-lock.json` | 工具自动生成，锁整棵依赖树 |
| Airflow 的 `--constraint` 文件 | 官方 curated lock | Airflow 官方测试过的几百个包版本 |

---

## 这个项目用的方案

```txt
# requirements.txt
apache-airflow==3.2.0
--constraint https://raw.githubusercontent.com/apache/airflow/constraints-3.2.0/constraints-3.12.txt
```

- `apache-airflow==3.2.0`：主包精确锁定
- `--constraint ...`：官方 lock 文件，锁定几百个依赖的版本

效果 ≈ `package.json`（写死版本）+ `package-lock.json`（依赖树锁定）一起用，**比只写 requirements.txt 更可靠**。

---

## 为什么 Python 没统一 lock 标准？

- Python 历史久，生态碎片化，pip 很晚才关注这个问题
- Node 的 npm 从设计之初就有 lock 的概念
- 现在 Python 社区逐渐往 `uv` / `poetry` 靠拢，有了更好的 lock 支持

---

## 一句话

| 概念 | 一句话 |
|------|--------|
| 不 lock | 「给我 2.x 以上的 pandas 就行」→ 装什么版本看运气 |
| lock | 「就要 pandas 2.1.4」→ 每次每人装都一样 |
| `py_env` ≈ `node_modules` | 本地依赖文件夹，不进 Git |
| `requirements.txt` ≈ `package.json` | 声明需要什么包 |
| constraint 文件 ≈ 官方 lock | Airflow 官方保证能一起工作的版本组合 |

**Python 把「声明」和「锁定」经常都塞进 `requirements.txt`，Node 分成两个文件。分开想就不乱。**

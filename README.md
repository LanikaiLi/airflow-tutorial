# Airflow Tutorial

Local Apache Airflow 3.2.0 development environment.

## Prerequisites

- Python **3.10+** (this project uses **3.12**)
- macOS: install via Homebrew if needed

```bash
brew install python@3.12
```

## Setup

```bash
git clone <your-repo-url>
cd airflow-tutorial

# Create and activate virtual environment
/opt/homebrew/bin/python3.12 -m venv py_env
source py_env/bin/activate

# Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# Set Airflow home directory (optional; defaults to ~/airflow)
export AIRFLOW_HOME="$PWD/airflow_home"
```

Add `AIRFLOW_HOME` to your shell profile if you want it set automatically:

```bash
export AIRFLOW_HOME=~/airflow-tutorial/airflow_home
```

## Run Airflow

```bash
source py_env/bin/activate
export AIRFLOW_HOME="$PWD/airflow_home"
export AIRFLOW__CORE__DAGS_FOLDER="$PWD/dags"
export AIRFLOW__CORE__LOAD_EXAMPLES="False"

airflow standalone
```

Open http://localhost:8080 — login credentials are in `airflow_home/simple_auth_manager_passwords.json.generated` (username is `admin`).

## Project Structure

```
airflow-tutorial/
├── dags/           # DAG files (create as needed)
├── py_env/         # virtual environment (gitignored)
├── airflow_home/   # Airflow config, DB, logs (gitignored)
├── requirements.txt
└── README.md
```

## Notes

- `py_env/` and `airflow_home/` are not committed. Each developer recreates them locally.
- Use Python 3.12 when installing; Airflow 3.2.0 does not support Python 3.9.

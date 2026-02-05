# dags/hello_schedule.py
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

with DAG(
    dag_id="hello_schedule",
    start_date=datetime(2024, 1, 1),
    schedule_interval="*/1 * * * *",  # 毎分
    catchup=False,
) as dag:

    BashOperator(
        task_id="say_hello",
        bash_command="date >> /opt/airflow/hello.log",
    )

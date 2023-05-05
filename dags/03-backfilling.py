from airflow import DAG
from airflow.operators.empty import EmptyOperator

from datetime import datetime

with DAG(
    dag_id='03-backfilling'
    , start_date=datetime(2022, 12, 25)
    , schedule='@daily'
    , catchup=True
    ) as dag:

    task1 = EmptyOperator(task_id='first_task')
    task2 = EmptyOperator(task_id='second_task')
    task3 = EmptyOperator(task_id='third_task')

    task1 >> [task2, task3]
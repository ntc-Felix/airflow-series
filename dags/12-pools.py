from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
import datetime

def wait_n_seconds(n):
    import time

    time.sleep(n)

@dag(
    dag_id='12-pools_example',
    start_date=datetime.datetime(2023,4,16),
    schedule=None
)
def example_pools():

    # Monthly
    t1 = PythonOperator(task_id='t1',pool='pool_example', priority_weight=1, python_callable=wait_n_seconds, op_args=[15])
    t2 = PythonOperator(task_id='t2',pool='pool_example', priority_weight=1, python_callable=wait_n_seconds, op_args=[15])
    t3 = PythonOperator(task_id='t3',pool='pool_example', priority_weight=1, python_callable=wait_n_seconds, op_args=[15])

    # Weekly
    t4 = PythonOperator(task_id='t4',pool='pool_example', priority_weight=5, python_callable=wait_n_seconds, op_args=[15])
    t5 = PythonOperator(task_id='t5',pool='pool_example', priority_weight=5, python_callable=wait_n_seconds, op_args=[15])
    t6 = PythonOperator(task_id='t6',pool='pool_example', priority_weight=5, python_callable=wait_n_seconds, op_args=[15])

    # Daily
    t7 = PythonOperator(task_id='t7',pool='pool_example', priority_weight=10, python_callable=wait_n_seconds, op_args=[15])
    t8 = PythonOperator(task_id='t8',pool='pool_example', priority_weight=10, python_callable=wait_n_seconds, op_args=[15])
    t9 = PythonOperator(task_id='t9',pool='pool_example', priority_weight=10, python_callable=wait_n_seconds, op_args=[15])


    t1 >> [t2,t3]

    t4 >> [t5,t6]

    t7 >> [t8, t9]

example_pools = example_pools()

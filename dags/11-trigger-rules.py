from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.decorators import task_group

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 4, 16),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('11-trigger_rules', default_args=default_args, schedule_interval='@daily')

t1 = BashOperator(
    task_id='t1',
    bash_command='echo "Hello from task 1"',
    dag=dag,
    trigger_rule = 'all_success',
    retries=3,
    retry_delay=timedelta(minutes=10),
    retry_exponential_backoff=False,
    max_retry_delay=timedelta(minutes=30)

)

@task_group(group_id='first_tg', dag=dag)
def dummy_task_group():

    t2 = BashOperator(
        task_id='t2',
        bash_command='echo "Hello from task 2"',
        dag=dag,
        trigger_rule = 'none_failed'
    )

    t3 = BashOperator(
        task_id='t3',
        bash_command='echo "Hello from task 3"',
        dag=dag,
        trigger_rule = 'one_failed'
    )

    t4 = BashOperator(
        task_id='t4',
        bash_command='echo "Hello from task 4"',
        dag=dag,
        trigger_rule = 'one_success'
    )

    [t2, t3, t4]

@task_group(group_id='second_tg', dag=dag)
def dummy_task_group2():
    t5 = BashOperator(
        task_id='t5',
        bash_command='echo "Hello from task 4"',
        dag=dag,
        trigger_rule = 'none_failed'
    )
    t6 = BashOperator(
        task_id='t6',
        bash_command='echo "Hello from task 4"',
        dag=dag,
        trigger_rule = 'none_skipped'
    )
    t7 = BashOperator(
        task_id='t7',
        bash_command='echo "Hello from task 4"',
        dag=dag,
        trigger_rule = 'all_done'
    )
    [t5,t6,t7]


t8 = BashOperator(
    task_id='t8',
    bash_command='echo "Hello from task 4"',
    dag=dag,
    trigger_rule = 'dummy'
)

first_tg = dummy_task_group()
second_tg = dummy_task_group2()

t1 >> first_tg >> second_tg >> t8

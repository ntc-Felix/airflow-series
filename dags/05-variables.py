from airflow import DAG
from airflow.models.variable import Variable
from airflow.operators.python import PythonOperator
import datetime
import time


DUMMY_VARIABLE = Variable.get(key='dummy_variable')
JSON_TEST = Variable.get(key='json_test', deserialize_json=True)


def dummy():
    print(f"{DUMMY_VARIABLE}")

def json_var_test():
    
    json_deserialized = JSON_TEST
    print(json_deserialized)
    print('#'*40)
    print(f"chave1:{json_deserialized['chave']} \nchave2:{json_deserialized['chave2']} \nchave3:{json_deserialized['chave3']}")


#S3_PATH = Variable.get(key='key')

with DAG(dag_id='05-variables', start_date=datetime.datetime(2023,2,12), schedule=None) as dag:

    task1 = PythonOperator(python_callable=dummy, task_id='task1')

    task2 = PythonOperator(python_callable=json_var_test, task_id='task2')

    task3 = PythonOperator(python_callable=dummy, task_id='task3')



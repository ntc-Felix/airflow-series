from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime

def funcao_exemplo(posicao:str):
    """
    Funcao responsavel por printar na tela um texto de teste

    Args:
        posicao(str): determina a posicao desejada para ser colocada na string
    """
    print(f'Testando minha {posicao} funcao python')

with DAG(dag_id='02-python_operator_example', start_date=datetime(2023, 1, 4), schedule=None) as dag:

    task1 = PythonOperator(
        task_id = 'primeira_funcao',
        python_callable = funcao_exemplo,
        op_args = ['primeira']
    )

    task2 = PythonOperator(
        task_id = 'segunda_funcao',
        python_callable = funcao_exemplo,
        op_kwargs = {
            'posicao' : 'segunda'
        }
    )

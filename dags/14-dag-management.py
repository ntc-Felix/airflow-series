from airflow.decorators import dag, task
import datetime

def _dummy_on_success_callback(context):
    return ("SUCCESS")

def _dummy_on_failure_callback(context):
    return ("FAILED")

def _dummy_on_retry_callback(context):
    if (context['ti'].try_number() > 2):
        pass
    return ("RETRYING")

def _pipeline_on_success_callback(context):
    return ("SUCCESS")

def _pipeline_on_failure_callback(context):
    # Did your task failed because of a timeout ?
    from airflow.exceptions import AirflowSensorTimeout, AirflowTaskTimeout
    if (context['exception']):
        if (isinstance(context['exception'], AirflowTaskTimeout)):
            pass
        elif (isinstance(context['exception'], AirflowSensorTimeout)):
            pass


    return ("FAILED")


@dag(
    dag_id='14-configs-test',
    start_date=datetime.datetime(2023,4,17),
    schedule='@daily',
    dagrun_timeout=datetime.timedelta(minutes=10),
    on_failure_callback=_pipeline_on_failure_callback,
    on_success_callback=_pipeline_on_success_callback,
)
def configs_test_pipeline(
    date: str,
    your_param: str,
    another_param: str
):
    # write your logic here

    @task(
            execution_timeout=datetime.timedelta(minutes=2),
            on_success_callback=_dummy_on_success_callback,
            on_failure_callback=_dummy_on_failure_callback,
            on_retry_callback=_dummy_on_retry_callback,
    )
    def dummy_task():
        return 1
    
configs_test_pipeline(date = '2023/04/16', your_param='foo', another_param='bar')
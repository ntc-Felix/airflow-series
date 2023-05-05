from airflow.decorators import task, dag
from airflow.sensors.base import PokeReturnValue

import datetime
from typing import Optional, List
import logging

import boto3

MINIO_USER = 'myaccesskey'
MINIO_KEY = 'mysecretkey'
MINIO_ENDPOINT_URL = "http://10.104.17.56:9000"

s3 = boto3.client(
    's3', 
    endpoint_url=MINIO_ENDPOINT_URL, 
    aws_access_key_id=MINIO_USER, 
    aws_secret_access_key=MINIO_KEY
)

s3_bucket = 'landing'
s3_key_prefix = "/market_random_data/json/"

@dag(
        dag_id='13-sensor_pipeline',
        start_date=datetime.datetime(2023,4,16),
        schedule=None
)
def sensor_pipeline():
    import time

    start_time = time.time()
    dt = datetime.datetime.now(datetime.timezone.utc)

    @task.sensor(poke_interval=5, timeout=3600, mode='poke')
    def minio_batch_of_files_sensor(
                                        s3_bucket: str, 
                                        s3_key_prefix: str, 
                                        number_of_files_to_be_processed: Optional[int] = 100,
                                    ) -> List:

        logger = logging.getLogger(__name__)

        # Check if any new files have been added since the most recent timestamp
        new_files = []
        response = s3.list_objects_v2(Bucket=s3_bucket, Prefix=s3_key_prefix)
        for obj in response.get('Contents', []):
            if obj.get('LastModified', dt) > dt:
                new_files.append(obj.get('Key'))

        elapsed_time = round(time.time() - start_time)

        logger.info(f"Found {len(new_files)} new files in {s3_bucket}/{s3_key_prefix} after {elapsed_time} seconds")

        if len(new_files) >= number_of_files_to_be_processed:
            globals()['dt'] = datetime.datetime.now(datetime.timezone.utc)
            return PokeReturnValue(is_done=True, xcom_value=new_files)
        else:
            return PokeReturnValue(is_done=False)
            
    
    @task
    def list_files(sensor_output: List):
        file_list = sensor_output
        return file_list

    @task
    def process_file(file):
        import time
        time.sleep(5)

        print(f"Processed file: {file}")

    sensor = minio_batch_of_files_sensor(s3_bucket=s3_bucket, s3_key_prefix=s3_key_prefix)
    files_list = list_files(sensor)
    process_files = process_file.expand(file=files_list)

    sensor >> files_list >> process_files

sensor_pipeline = sensor_pipeline()



    

    
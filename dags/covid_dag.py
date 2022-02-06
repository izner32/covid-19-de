from datetime import timedelta
import airflow 
from airflow import DAG
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
import pandas as pd
import os 
from plugins.operators.create_s3_bucket_operator import CreateS3BucketOperator
from plugins.operators.local_dir_to_s3_bucket_operator import LocalDirToS3BucketOperator
import logging

KEY = Variable.get('USER_ACCESS_KEY')
SECRET = Variable.get('USER_SECRET_KEY')
REGION = Variable.get('REGION_NAME')

# creating dag
default_args = {
    'owner': 'airflow',    
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
	dag_id = "covid_dag",
    default_args=default_args,
    start_date = datetime.today(),
	schedule_interval='@once',	
)

# tasks/jobs on the dag 
bucket_name='covid-dataset-files'
file_path='data/raw'
create_s3_bucket = CreateS3BucketOperator(
    task_id='create_s3_bucket', 
    dag = dag, 
    bucket_name=bucket_name,
    aws_credentials={
        'KEY': KEY,
        'SECRET': SECRET,
        'REGION': REGION
    }
)

local_dir_to_s3_bucket = LocalDirToS3BucketOperator(
    task_id='local_dir_to_s3_bucket', 
    dag = dag, 
    bucket_name=bucket_name,
    file_path = file_path,
    aws_credentials={
        'KEY': KEY,
        'SECRET': SECRET,
        'REGION': REGION
    }
)


create_s3_bucket >> local_dir_to_s3_bucket
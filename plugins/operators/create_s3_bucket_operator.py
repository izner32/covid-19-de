import boto3 
import os 
import subprocess
from airflow.models import BaseOperator 
from airflow.utils.decorators import apply_defaults 
from airflow import DAG 

class CreateS3BucketOperator(BaseOperator):
    @apply_defaults 
    def __init__(self,
                bucket_name = '',
                aws_credentials = {},
                *args,
                **kwargs):

        super(CreateS3BucketOperator, self).__init__(*args, **kwargs)
        self.bucket_name = bucket_name 
        self.aws_credentials = aws_credentials
    
    def execute (self,context):
        # connect to aws 
        s3 = boto3.client(
            's3',
            region_name=self.aws_credentials.get('REGION'),
            aws_access_key_id=self.aws_credentials.get('KEY'),
            aws_secret_access_key=self.aws_credentials.get('SECRET')
        )

        # create s3 bucket 
        bucket_list = s3.list_buckets()['Buckets']
        if self.bucket_name not in bucket_list: 
            covid_dataset = s3.create_bucket(
                Bucket = self.bucket_name
            )
        else: 
            print('bucket-name already exists')

    
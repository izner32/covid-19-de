import boto3 
import os 
import subprocess
from airflow.models import BaseOperator 
from airflow.utils.decorators import apply_defaults 
from airflow import DAG 
import logging

class LocalDirToS3BucketOperator(BaseOperator):
    @apply_defaults 
    def __init__(self,
                bucket_name = '',
                file_path = '',
                aws_credentials = {},
                *args,
                **kwargs):

        super(LocalDirToS3BucketOperator, self).__init__(*args, **kwargs)
        self.bucket_name = bucket_name 
        self.file_path = file_path
        self.aws_credentials = aws_credentials
    
    def execute (self,context):
        # connect to aws 
        s3 = boto3.client(
            's3',
            region_name=self.aws_credentials.get('REGION'),
            aws_access_key_id=self.aws_credentials.get('KEY'),
            aws_secret_access_key=self.aws_credentials.get('SECRET')
        )

        for root,dirs,files in os.walk(self.file_path):
            for file in files:
                s3.upload_file(os.path.join(root,file),self.bucket_name,file)

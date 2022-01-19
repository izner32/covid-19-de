# this is only if we want to upload the all of the files belonging to a directory 
# but if we're uploading directories insteda of files, it's better to do it manually, it's just drag and drop at s3 console

import boto3 
import os 
from dotenv import load_dotenv 

load_dotenv() 

# connect to aws 
KEY = os.getenv('S3_USER_ACCESS_KEY')
SECRET = os.getenv('S3_USER_SECRET_KEY')

s3 = boto3.client(
   's3',
   region_name="us-east-1",
   aws_access_key_id=KEY,
   aws_secret_access_key=SECRET
)

# create s3 bucket 
bucketname = "covid-dataset-files"
covid_dataset = s3.create_bucket(
    Bucket = bucketname
)

# upload the objects(files) to the bucket
filepath = "D:/Renz/C - Programming/A - Projects/covid_19/source/data"
def upload_directories(filepath, bucketname):
    for root,dirs,files in os.walk(filepath):
        for file in files:
            s3.upload_file(
                os.path.join(root,file),
                bucketname,
                file
            )

upload_directories(filepath, bucketname)

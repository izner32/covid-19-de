import boto3 
import configparser 
import os 
from dotenv import load_dotenv 

load_dotenv() 

# connect to aws 
KEY = os.getenv('AWS_KEY')
SECRET = os.getenv('AWS_SECRET')

s3 = boto3.resource(
   's3',
   region_name="us-west-2",
   aws_access_key_id=KEY,
   aws_secret_access_key=SECRET
)

# create s3 bucket 
covid_dataset = s3.create_bucket(
    Bucket = 'covid_dataset' 
)

# upload the objects(files/dirs) to the bucket
filepath = "../source/data"
def get_directories():
    for root, dirs, files in os.walk(filepath):
        return dirs 

for dir in get_directories():
    s3.upload_file(
        "../source/data/{}".format(dir),
        'covid_dataset',  
        dir
    )
s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-2',
    aws_access_key_id='mykey',
    aws_secret_access_key='mysecretkey'
)

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
    
import os
os.environ["AWS_DEFAULT_REGION"] = 'us-east-2'
os.environ["AWS_ACCESS_KEY_ID"] = 'mykey'
os.environ["AWS_SECRET_ACCESS_KEY"] = 'mysecretkey'

# Upload files to S3 bucket
def localToS3(fileName):
    s3.Bucket('Harih').upload_file(Filename= fileName , Key= fileName)

# Download files from s3 to localhost
def S3ToLocal(fileName):
    s3 = boto3.client('s3')
    s3.download_file('Harih', 'downloaded.csv', fileName)

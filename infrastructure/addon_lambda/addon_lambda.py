#!usr/bin/env python3

## lambda to copy extra/ custom addon .zip file from addon bucket to EFS mount 
## shared with odoo containers, triggered when a file is uploaded to the addon bucket.

from boto3 import client
from json import dumps
from urllib import parse
from shutil import unpack_archive
from os import remove, listdir

s3 = client('s3')
ecs_cluster = client('ecs')

file_path = '/mnt/extra-addons/'

def download_zip(bucket, key):
    try:
        s3.download_file(bucket, key, file_path+key)
        print(f'{key} successfully collected from {bucket}.')
    except Exception as error:
        print(f'Error getting object {key} from bucket {bucket}: {error}')

def clear_bucket(bucket, key):
    try:
        s3.delete_object(Bucket=bucket, Key=key)
        print(f'{key} deleted from {bucket}.')
    except Exception as error:
        print(f'Clear Bucket Error: {error}')

def unpack_zip(key):
    try:
        unpack_archive(file_path+key, file_path, 'zip')
        print(f'{key} unpack complete.')
    except Exception as error:
        print(f'Unpack Error: {error}')

def remove_zip(key):
    try:
        remove(file_path+key)
        print(f'{key} deleted.')
    except Exception as error:
        print(f'{key} delete error: {error}')
    
## restart_odoo currently errors, addon installs ok, more tests needed to determine if required.
def restart_odoo():
    try:
        ecs_cluster.execute_command(command='/etc/init.d/odoo restart',
            interactive = False,
            task = 'odooFargateService')
    except Exception as error:
        print(f'Odoo restart error: {error}')

 ## listens for event created when file uploaded to S3 bucket
def lambda_handler(event, context):
    #print("Received event: " + dumps(event, indent=2))

    # get bucket name and file name (key) from upload event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    # download zip file from bucket to mount point
    download_zip(bucket, key)
    # delete zip file from bucket
    clear_bucket(bucket, key)
    # use shutil to unzip file
    unpack_zip(key)
    # use os to remove .zip from efs
    remove_zip(key)
    #dir_content = listdir(file_path)
    
    # restart containers ??
    #restart_odoo()

    print(f'Finished, addon successfully loaded?')
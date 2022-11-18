#!/usr/bin/env python3

## Dev only! No security implimented!
## API endpoint for running CLI commands in lambda. Can navigate to EFS /mnt/extra-addons/ 
## or another mount if needed, change or add mounts in eleos_stack.py.
## Useful for debugging, can manage files in EFS, may have uses in the future. Perhaos the start 
## of a little web app EFS file manager secured with Cognito, if that is ever needed.
## example request "curl -X POST -H 'Content-Type: text/plain' -d 'ls -la' https://apiendpointURL...."


from subprocess import run, PIPE
from shlex import split

def run_cmd(command):
    splt_cmd = split(command)
    try:
        process = run(splt_cmd, stdout=PIPE, universal_newlines=True)
    except Exception as error:
        print(f'Error: {error}')
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/plain'
                },
            'body': '> {}\n'.format(error)
            }
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
            },
        'body': '> {}\n{}'.format(command, process.stdout)
        }


## Triggered by API request
def lambda_handler(event, context):
    #print(event)
    method = event['requestContext']['httpMethod']
    if method == 'POST':
        cmd = event['body']
        response = run_cmd(cmd)
    else:
        response = {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/plain'
                },
            'body': 'Method Unsupported'
            }
    return response
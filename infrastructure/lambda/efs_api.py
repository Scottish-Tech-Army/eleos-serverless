#!/usr/bin/env python3

from os import listdir, remove
#import fcntl

MSG_FILE_PATH = '/mnt/extra-addons/messages.txt'

def get_files(path):
    try:
        files = listdir(path)
    except Exception as error:
        reply = f'Error: {error}'
    return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/plain'
                },
            'body': 'Files: \n{}\n'.format(files)
            }

def get_messages():
    try:
        with open(MSG_FILE_PATH, 'a+') as msg_file:
            #fcntl.flock(msg_file, fcntl.LOCK_SH)
            msg_file.seek(0)
            messages = msg_file.read()
            #fcntl.flock(msg_file, fcntl.LOCK_UN)
    except Exception as error:
        print(error)
        messages = f'Error: {error}'
    if messages == '':
        messages = 'No messages'
    return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/plain'
                },
            'body': 'Messages:\n{}\n'.format(messages)
            }

def add_message(new_message):
    try:
        with open(MSG_FILE_PATH, 'a') as msg_file:
            #fcntl.flock(msg_file, fcntl.LOCK_EX)
            msg_file.write(new_message + "\n")
            #fcntl.flock(msg_file, fcntl.LOCK_UN)
    except Exception as error:
        print(f'Add message error :{error}')

def delete_messages():
    try:
        remove(MSG_FILE_PATH)
    except:
        pass

def lambda_handler(event, context):
    #print(event)
    method = event['requestContext']['httpMethod']
    if method == 'GET':
        path = event['body']
        messages = get_files(path)
    elif method == 'POST':
        path = event['body']
        #add_message(new_message)
        messages = get_files(path)
    elif method == 'DELETE':
        delete_messages()
        messages = 'Messages deleted.'
    else:
        messages = 'Method unsupported.'
    return messages
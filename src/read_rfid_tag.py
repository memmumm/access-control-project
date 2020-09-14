#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import boto3

reader = SimpleMFRC522()
sns = boto3.client('sns')

def read_rfid_tag():

        try:
                tagid, userid = reader.read()
                print(f'Processing read event...')
                return userid
        finally:
                GPIO.cleanup()

def send_user_id_to_sns(userid):
        sns.publish(
                TopicArn='read event topic arn',
                Message={
                        "userId": userid
                },
                Subject=f'Read event for {userid}'
        )

send_user_id_to_sns(read_rfid_tag())
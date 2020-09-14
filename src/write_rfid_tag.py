#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import uuid
import boto3

reader = SimpleMFRC522()
sns = boto3.client('sns')

def write_rfid_tag():
    try:
        firstname = input('Please enter your first name: ')
        lastname = input ('Please enter your last name: ')
        print("Now place your tag to write")
        userid = reader.write(uuid.uuid4())
        print("Tag written")

        return [userid, firstname, lastname]

    except:
        print("There was an error, please try running the script again")
        return

    finally:
        GPIO.cleanup()

def send_user_info_to_sns(userinfo):

    sns.publish(
        TopicArn='write event topic arn',
        Message={
            "userId": userinfo[0],
            "firstName": userinfo[1],
            "lastName": userinfo[2]
        },
        Subject=f'Write event for {userinfo[0]}'
    )

send_user_info_to_sns(write_rfid_tag())
#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import uuid
import boto3
import json

reader = SimpleMFRC522()
sns = boto3.client('sns')

def write_rfid_tag():
    try:
        firstname = input('Please enter your first name: ')
        lastname = input ('Please enter your last name: ')
        print("Now place your tag to write")
        tag_id = reader.write(str(uuid.uuid4()))
        userid = tag_id[1]
        print("Tag written")
        response = [userid, firstname, lastname]
        return response

    except:
        print("There was an error, please try running the script again")
        return

    finally:
        GPIO.cleanup()

def send_user_info_to_sns(userdata):
    
    message = json.dumps(
	{
            "userId": userdata[0],
            "firstName": userdata[1],
            "lastName": userdata[2]
        })
    sns.publish(
        TopicArn='arn:aws:sns:us-east-1:821383200340:WriteTagTopic',
        Message=message,
        Subject='Write event for {user}'.format(user=userdata[0])
    )

writeresponse = write_rfid_tag()
send_user_info_to_sns(writeresponse)

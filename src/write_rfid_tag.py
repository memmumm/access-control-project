#!/usr/bin/env python
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import uuid
import boto3

reader = SimpleMFRC522()

def write_rfid_tag():
    try:
        firstname = input('Please enter your first name: ')
        lastname = input ('Please enter your last name: ')
        print("Now place your tag to write")
        userid = reader.write(uuid.uuid4())
        print("Tag written")

        return [firstname, lastname, userid]

    except:
        print("There was an error, please try running the script again")
        return

    finally:
        GPIO.cleanup()

def send_user_info_to_db(userinfo):
    pass
    # tähän tulee funktio, joka lähettää syötetyn userinfon SNS-topikkiin

send_user_info_to_db(write_rfid_tag())
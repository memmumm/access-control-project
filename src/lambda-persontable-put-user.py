import json
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('person')

def create_new_user(event, context):

    jsondata = json.loads(event)
    item = {
        'id': str(jsondata['userId']),
        'firstname': jsondata['firstName'],
        'lastname': jsondata['lastName'],
    }
    table.put_item(Item=item)

    return {
        "id": jsondata['userId']
    }





import boto3

client = boto3.client('rekognition', 'us-east-1')

def compare_faces():
    response = client.compare_faces(
        SimilarityThreshold=90,
        SourceImage={
            'S3Object': {
                'Bucket': 'rasberry-bucket',
                'Name': 'MerviSiipilahde.png'
            }
        },
        TargetImage={
            'S3Object': {
                'Bucket': 'rasberry-bucket',
                'Name': 'MitjaHaimila.jpg'
            }
        }
    )

    print(response)

compare_faces()
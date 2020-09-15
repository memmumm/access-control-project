import boto3
import picamera

def take_picture():

    camera = picamera.PiCamera()
    camera.capture('example.jpg')

def upload_photo():
    s3 = boto3.resource('s3')
    BUCKET = "rasberry-bucket"

    #dumppaa paikallisesta tiedostosta kansion "testi/dumppi" rasberry-bucketiin
    s3.Bucket(BUCKET).upload_file("/home/pi/example.jpg", "testi/dumppi")
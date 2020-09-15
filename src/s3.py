import boto3

s3 = boto3.resource('s3')
BUCKET = "rasberry-bucket"

#dumppaa paikallisesta tiedostosta kansion "testi/dumppi" rasberry-bucketiin
s3.Bucket(BUCKET).upload_file("C:/Users/Yoda/Desktop/file1.png", "testi/dumppi")
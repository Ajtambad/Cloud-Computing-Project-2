#__copyright__   = "Copyright 2024, VISA Lab"
#__license__     = "MIT"

from boto3 import client as boto3_client
import subprocess
import os
import time

stage_1_bucket = '1229560048-stage-1'
input_bucket = '1229560048-input'

s3 = boto3_client('s3', region_name='us-east-1')

def handler(event, context):

    video_filename = event['Records'][0]['s3']['object']['key']
    filename = video_filename
    video_filename = os.path.join('/tmp', video_filename)
    file = s3.download_file(input_bucket, filename, video_filename) #Download from input S3 bucket
    filename = os.path.basename(video_filename)
    outdir = os.path.splitext(filename)[0]
    outdir = os.path.join("/tmp",outdir)

    if not os.path.exists(outdir):
        os.makedirs(outdir)

    split_cmd = '/usr/bin/ffmpeg -ss 0 -r 1 -i ' +video_filename+ ' -vf fps=1/10 -start_number 0 -vframes 10 ' + outdir + "/" + 'output_%02d.jpg -y'
    try:
        subprocess.check_call(split_cmd, shell=True)
    except subprocess.CalledProcessError as e:
        print(e.returncode)
        print(e.output)

    #Upload to Stage-1 S3 Bucket
    dir = os.listdir(outdir)
    for file in dir:
        s3.upload_file(outdir + '/' + file, stage_1_bucket, filename.split('.')[0] + '/{}'.format(file))
    time.sleep(2)
    return outdir

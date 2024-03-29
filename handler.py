#__copyright__   = "Copyright 2024, VISA Lab"
#__license__     = "MIT"

from boto3 import client as boto3_client
import subprocess
import math
import os

stage_1_bucket = '1229560048-stage-1'
s3 = boto3_client('s3', region_name='us-east-1')

# def handler(event, context):
def handler():

    # video_filename = event['Records'][0]['s3']['object']['key']
    video_filename = '/test_2.mp4'
    filename = os.path.basename(video_filename)
    outdir = os.path.splitext(filename)[0]
    outdir = os.path.join("/tmp",outdir)
    output_dir = outdir
    
    # s3.put_object(Key=(filename.split('.')[0] + '/'))
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    split_cmd = '/usr/bin/ffmpeg -ss 0 -r 1 -i ' +video_filename+ ' -vf fps=1/10 -start_number 0 -vframes 10 ' + outdir + "/" + 'output-%02d.jpg -y'
    try:
        subprocess.check_call(split_cmd, shell=True)
    except subprocess.CalledProcessError as e:
        print(e.returncode)
        print(e.output)

    dir = os.listdir(outdir)
    for file in dir:
        s3.upload_file(outdir + '/' + file, stage_1_bucket, filename.split('.')[0] + '/{}'.format(file))

    fps_cmd = 'ffmpeg -i ' + video_filename + ' 2>&1 | sed -n "s/.*, \\(.*\\) fp.*/\\1/p"'
    fps = subprocess.check_output(fps_cmd, shell=True).decode("utf-8").rstrip("\n")
    fps = math.ceil(float(fps))
    print(outdir)
    print(fps)
    return outdir

if __name__=='__main__':
    handler()

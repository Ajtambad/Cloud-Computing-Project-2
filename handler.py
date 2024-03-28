#__copyright__   = "Copyright 2024, VISA Lab"
#__license__     = "MIT"

from boto3 import client as boto3_client


def handler(event, context):
    # print(event)
    # print("Hello boss")
    video_filename = event['Records'][0]['s3']['object']['key']
    print(video_filename)
	# filename = os.path.basename(video_filename)
    # outdir = os.path.splitext(filename)[0]
    # outdir = os.path.join("/tmp",outdir)
    # output_dir = outdir
    # if not os.path.exists(outdir):
    #     os.makedirs(outdir)

    # split_cmd = '/usr/bin/ffmpeg -ss 0 -r 1 -i ' +video_filename+ ' -vf fps=1/10 -start_number 0 -vframes 10 ' + outdir + "/" + 'output-%02d.jpg -y'
    # try:
    #     subprocess.check_call(split_cmd, shell=True)
    # except subprocess.CalledProcessError as e:
    #     print(e.returncode)
    #     print(e.output)

    # fps_cmd = 'ffmpeg -i ' + video_filename + ' 2>&1 | sed -n "s/.*, \\(.*\\) fp.*/\\1/p"'
    # fps = subprocess.check_output(fps_cmd, shell=True).decode("utf-8").rstrip("\n")
    # fps = math.ceil(float(fps))
    # return outdir

{'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'us-east-1', 'eventTime': '2024-03-27T21:38:39.475Z', 
              'eventName': 'ObjectCreated:Put', 'userIdentity': {'principalId': 'A2OTPLWQ08QZC3'}, 'requestParameters': {'sourceIPAddress': '129.219.21.44'}, 
              'responseElements': {'x-amz-request-id': '5SK7F01TKX1BEQ50', 'x-amz-id-2': 'czj4AUlJS99oXRwwO/P4iXOaqK2bktpyHK3i4h0Ofg5alWlOyubtabgf+4ytL1MGTMH5gNY05onbBhT5o8+SndgdTSCc4lQw'}, 
              's3': {'s3SchemaVersion': '1.0', 'configurationId': 'ec601d40-003e-4c0d-97a4-c74ad3989093', 'bucket': {'name': '1229560048-input', 'ownerIdentity': {'principalId': 'A2OTPLWQ08QZC3'}, 
                'arn': 'arn:aws:s3:::1229560048-input'}, 'object': {'key': 'test_2.mp4', 'size': 418298, 'eTag': '400ca61b39ea2d349a65e6b03d52fae4', 'sequencer': '00660491DF5C94558C'}}}]}
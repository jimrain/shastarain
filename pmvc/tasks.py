from celery import shared_task,current_task
from numpy import random
from scipy.fftpack import fft
# from .models import Company, WorkOrder, VideoJobState, REGULAR_PRIORITY, LOW_
from .models import Video
import shastarain.settings as settings
import boto3

@shared_task
def fft_random(n):
    """
    Brainless number crunching just to have a substantial task:
    """
    for i in range(n):
        x = random.normal(0, 0.1, 2000)
        y = fft(x)
        if(i%30 == 0):
            process_percent = int(100 * float(i) / float(n))
            current_task.update_state(state='PROGRESS',
                                      meta={'process_percent': process_percent})
    return random.random()

@shared_task
def add(x,y):
    for i in range(1000000000):
        a = x+y
    return x+y

@shared_task
def handle_ingest_video(video_id, dm):
    video = Video.objects.get(pk=video_id)
    # Need to check the file extension - assuming mp4 for now.
    filename = 'videos/' + video.title + '/digital_master.mp4'
    # file = request.FILES['upload']
    s3 = boto3.resource('s3', aws_access_key_id=settings.AWS_ACCESS_KEY,
                        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    bucket = s3.Bucket(settings.AWS_VIDEO_BUCKET)
    bucket.put_object(Key=filename, Body=dm)

    # print (dm.name)

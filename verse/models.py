from django.db import models
from django.contrib.auth.models import AbstractUser
# from verser.models import CustomUser
from video.models import Video


class Post(models.Model):
    # opponent , on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
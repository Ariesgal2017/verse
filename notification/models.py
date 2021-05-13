from django.db import models
from verser.models import CustomUser
from django.utils import timezone

# Got help from Detrich Schilling in study hall.
# Create your models here.
class Notification(models.Model):
    seen = models.BooleanField(default=False)
    user_notify = models.ForeignKey(CustomUser, related_name='usernotify', on_delete=models.CASCADE)

    
    def __str__(self):
        return (self.tweet_notify.content)



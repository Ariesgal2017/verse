from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    display_name = models.CharField(max_length=60, unique=True)
    losses = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)

    def __str__(self):
        return self.username
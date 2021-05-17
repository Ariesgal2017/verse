from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
# Create your models here.
class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    display_name = models.CharField(max_length=60, unique=True)
    losses = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)

    def __str__(self):
        return self.username
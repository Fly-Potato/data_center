from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=255, default=None, help_text="昵称")

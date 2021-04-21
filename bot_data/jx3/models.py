from django.db import models


class DaZhan(models.Model):
    bid = models.IntegerField("副本ID")
    fuben = models.CharField("副本", max_length=255)

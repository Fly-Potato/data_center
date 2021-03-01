from django.db import models


class Material(models.Model):
    name = models.CharField(max_length=255)
    level = models.IntegerField()
    attribute = models.CharField(max_length=255)
    attribute_num = models.IntegerField()
    type = models.CharField(max_length=255)
    addr = models.TextField()

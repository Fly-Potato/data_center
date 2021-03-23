from django.db import models


class VersionModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    version = models.CharField(max_length=255)
    update_log = models.TextField(default="")

    def __str__(self):
        return self.name

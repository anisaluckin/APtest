from django.db import models

class Video(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)

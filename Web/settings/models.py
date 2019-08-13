from __future__ import unicode_literals
from django.db import models
# Create your models here


class Settings(models.Model):
    settings_name = models.TextField()
    settings_pic = models.TextField()
    settings_pic_url = models.TextField()
    settings_head = models.TextField()
    settings_title = models.TextField()

    def __str__(self):
        return self.settings_name

from __future__ import unicode_literals
from django.db import models
# Create your models here


class Slide(models.Model):
    slide_name = models.TextField()
    slide_pic = models.TextField()
    slide_pic_url = models.TextField()

    def __str__(self):
        return self.slide_name

from __future__ import unicode_literals
from django.db import models
# Create your models here
# Create your models here
# Create your models here


class News(models.Model):
    news_titel = models.CharField(max_length=30)
    news_pic = models.TextField()
    news_url = models.TextField()
    date = models.TextField(default="_")
    news_short_txt = models.TextField()
    news_body_txt = models.TextField()

    def __str__(self):
        return self.news_titel

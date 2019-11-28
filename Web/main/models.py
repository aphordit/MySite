from __future__ import unicode_literals
from django.db import models
# Create your models here
# Create your models here
# Create your models here


class Main(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.TextField()
    number = models.IntegerField()

    def __str__(self):
        return self.first_name

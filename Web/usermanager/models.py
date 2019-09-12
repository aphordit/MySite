from __future__ import unicode_literals
from django.db import models
# Create your models here



class Usermanager(models.Model):
    uname = models.CharField(max_length=30)
    email = models.TextField()
    date = models.TextField(default="_")
    about = models.TextField()
    birth = models.TextField()
    level = models.TextField()
    group = models.TextField(default="admin_level_1")

    def __str__(self):
        return self.uname

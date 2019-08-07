from __future__ import unicode_literals
from django.db import models
# Create your models here


class Menu(models.Model):
    menu_name = models.TextField()
    menu_titel = models.TextField()
    menu_link = models.TextField()

    def __str__(self):
        return self.menu_name

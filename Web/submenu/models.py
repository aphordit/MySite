from __future__ import unicode_literals
from django.db import models


class Submenu(models.Model):
    sub_name = models.TextField()
    menu_name = models.TextField()
    menu_id = models.IntegerField()

    def __str__(self):
        return self.sub_name

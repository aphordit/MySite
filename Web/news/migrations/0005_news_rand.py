# Generated by Django 2.2.3 on 2019-11-14 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20191024_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='rand',
            field=models.IntegerField(default=0),
        ),
    ]

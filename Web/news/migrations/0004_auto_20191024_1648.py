# Generated by Django 2.2.3 on 2019-10-24 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20190822_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='menu_id',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='news',
            name='submenu_id',
            field=models.IntegerField(default=6),
        ),
    ]

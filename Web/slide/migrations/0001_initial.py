# Generated by Django 2.2.3 on 2019-07-30 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slide_name', models.TextField()),
                ('slide_pic', models.TextField()),
                ('slide_pic_url', models.TextField()),
            ],
        ),
    ]
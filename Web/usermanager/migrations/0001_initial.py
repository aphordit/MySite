# Generated by Django 2.2.3 on 2019-09-12 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usermanager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=30)),
                ('upass', models.TextField()),
                ('email', models.TextField()),
                ('date', models.TextField(default='_')),
                ('about', models.TextField()),
                ('birth', models.TextField()),
                ('level', models.TextField()),
            ],
        ),
    ]

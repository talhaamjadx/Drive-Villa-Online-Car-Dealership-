# Generated by Django 3.0.4 on 2020-04-07 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DriveVilla', '0003_auto_20200407_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, unique=True),
        ),
    ]
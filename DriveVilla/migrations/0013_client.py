# Generated by Django 3.0.4 on 2020-05-04 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DriveVilla', '0012_auto_20200424_1543'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('channel_name', models.CharField(max_length=400)),
            ],
        ),
    ]

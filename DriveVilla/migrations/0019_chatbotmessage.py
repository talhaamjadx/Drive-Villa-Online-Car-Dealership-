# Generated by Django 3.0.4 on 2020-05-21 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DriveVilla', '0018_delete_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatBotMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=300)),
                ('response', models.CharField(max_length=300)),
            ],
        ),
    ]

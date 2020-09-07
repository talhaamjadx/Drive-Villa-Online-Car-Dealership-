# Generated by Django 3.0.4 on 2020-05-04 17:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DriveVilla', '0014_chatmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='reciepent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_reciever', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_sender', to=settings.AUTH_USER_MODEL),
        ),
    ]
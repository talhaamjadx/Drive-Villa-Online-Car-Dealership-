# Generated by Django 3.0.4 on 2020-09-03 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DriveVilla', '0028_chatbotmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatbotmessage',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

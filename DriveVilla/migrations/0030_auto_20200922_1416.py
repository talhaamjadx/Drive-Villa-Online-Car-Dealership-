# Generated by Django 3.0.4 on 2020-09-22 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('DriveVilla', '0029_auto_20200903_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatbotmessage',
            name='ad_seller',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='ad_seller', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chatbotmessage',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ad_customer', to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 3.0.4 on 2020-04-14 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DriveVilla', '0007_auto_20200414_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
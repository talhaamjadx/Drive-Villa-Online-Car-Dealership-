# Generated by Django 3.0.4 on 2020-04-24 10:36

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('DriveVilla', '0010_auto_20200414_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adimage',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
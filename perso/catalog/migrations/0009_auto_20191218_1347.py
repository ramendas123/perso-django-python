# Generated by Django 2.0.3 on 2019-12-18 13:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20191218_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2019, 12, 18, 13, 47, 39, 648563, tzinfo=utc)),
        ),
    ]

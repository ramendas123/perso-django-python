# Generated by Django 2.0.3 on 2019-12-17 12:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20191217_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2019, 12, 17, 12, 0, 15, 962518, tzinfo=utc)),
        ),
    ]

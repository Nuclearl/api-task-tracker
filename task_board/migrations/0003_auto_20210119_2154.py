# Generated by Django 3.1.5 on 2021-01-19 21:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('task_board', '0002_auto_20210119_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 19, 21, 54, 41, 322527, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='board',
            name='modified_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 19, 21, 54, 41, 322559, tzinfo=utc)),
        ),
    ]

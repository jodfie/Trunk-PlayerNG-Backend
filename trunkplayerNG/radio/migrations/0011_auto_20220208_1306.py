# Generated by Django 3.2.10 on 2022-02-08 21:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0010_auto_20220204_2036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transmission',
            options={'ordering': ['-startTime']},
        ),
        migrations.AlterField(
            model_name='systemreciverate',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 8, 13, 6, 51, 18644)),
        ),
    ]

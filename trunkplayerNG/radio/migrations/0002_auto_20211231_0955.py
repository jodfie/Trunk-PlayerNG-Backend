# Generated by Django 3.2.8 on 2021-12-31 17:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemforwarder',
            name='forwardIncidents',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='transmission',
            name='locked',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='systemreciverate',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 31, 9, 55, 19, 815456)),
        ),
    ]

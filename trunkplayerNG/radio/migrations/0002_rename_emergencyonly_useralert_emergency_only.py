# Generated by Django 3.2.10 on 2022-03-13 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useralert',
            old_name='emergencyOnly',
            new_name='emergency_only',
        ),
    ]
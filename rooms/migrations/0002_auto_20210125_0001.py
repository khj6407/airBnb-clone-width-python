# Generated by Django 2.2.5 on 2021-01-24 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='chech_in',
            new_name='check_in',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='chech_out',
            new_name='check_out',
        ),
    ]

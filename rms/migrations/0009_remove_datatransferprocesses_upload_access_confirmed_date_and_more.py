# Generated by Django 4.1.6 on 2024-06-20 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0008_rename_initial_contact_date_datatransferprocesses_set_up_start_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datatransferprocesses',
            name='upload_access_confirmed_date',
        ),
        migrations.RemoveField(
            model_name='datatransferprocesses',
            name='upload_access_requested_date',
        ),
    ]

# Generated by Django 4.1.6 on 2024-07-01 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0009_remove_datatransferprocesses_upload_access_confirmed_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datauseprocesses',
            old_name='access_confirmed_date',
            new_name='availability_expiry_date',
        ),
        migrations.RenameField(
            model_name='datauseprocesses',
            old_name='set_up_completed_date',
            new_name='set_up_complete_date',
        ),
        migrations.RenameField(
            model_name='datauseprocesses',
            old_name='initial_contact_date',
            new_name='set_up_start_date',
        ),
        migrations.RemoveField(
            model_name='datauseprocesses',
            name='availability_confirmed_date',
        ),
    ]

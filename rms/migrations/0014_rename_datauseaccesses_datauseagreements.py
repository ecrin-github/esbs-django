# Generated by Django 4.1.6 on 2024-11-18 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rms', '0013_rename_datatransferaccesses_datatransferagreements'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DataUseAccesses',
            new_name='DataUseAgreements',
        ),
    ]

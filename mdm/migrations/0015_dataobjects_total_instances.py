# Generated by Django 4.1.6 on 2024-07-31 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdm', '0014_objectinstances_sd_iid'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataobjects',
            name='total_instances',
            field=models.IntegerField(default=0),
        ),
    ]

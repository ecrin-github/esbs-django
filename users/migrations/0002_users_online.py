# Generated by Django 4.1.6 on 2024-08-21 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='online',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 4.1.6 on 2024-04-25 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdm', '0002_dataobjects_organisation_studies_organisation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataobjects',
            name='access_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='objecttitles',
            name='title_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studytitles',
            name='title_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
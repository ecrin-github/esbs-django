# Generated by Django 4.1.6 on 2024-05-27 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mdm', '0005_remove_studyrelationships_target_study_id_and_more'),
    ]

    operations = [
        # Note: Postgresql sequences cannot be created with Django so you have to create it manually
        # This migration file just sets the sequence to the correct starting number

        # migrations.CreateModel(
        #     name='StudyNumberSeq',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('last_value', models.IntegerField()),
        #         ('increment_by', models.IntegerField()),
        #         ('max_value', models.IntegerField()),
        #         ('min_value', models.IntegerField()),
        #         ('cache_value', models.IntegerField()),
        #         ('log_cnt', models.IntegerField()),
        #         ('is_cycled', models.BooleanField()),
        #         ('is_called', models.BooleanField()),
        #     ],
        #     options={
        #         'db_table': 'study_number_seq',
        #     },
        # ),
        migrations.RunSQL(
            "ALTER SEQUENCE study_number_seq RESTART"
        ),
        migrations.RunSQL(
            "SELECT nextval('study_number_seq') from study_number_seq"
        ),
    ]

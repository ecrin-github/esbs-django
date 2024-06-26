# Generated by Django 4.1.6 on 2024-04-18 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
        ('context', '0001_initial'),
        ('mdm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataobjects',
            name='organisation',
            field=models.ForeignKey(blank=True, db_column='organisation_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='data_objects_organisation_id', to='general.organisations'),
        ),
        migrations.AddField(
            model_name='studies',
            name='organisation',
            field=models.ForeignKey(blank=True, db_column='organisation_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='studies_organisation_id', to='general.organisations'),
        ),
        migrations.AlterField(
            model_name='objecttopics',
            name='original_value',
            field=models.ForeignKey(blank=True, db_column='original_value', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='object_topics_original_value', to='context.topicvocabularies'),
        ),
        migrations.AlterField(
            model_name='studytopics',
            name='original_value',
            field=models.ForeignKey(blank=True, db_column='original_value', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='study_topics_original_value', to='context.topicvocabularies'),
        ),
    ]

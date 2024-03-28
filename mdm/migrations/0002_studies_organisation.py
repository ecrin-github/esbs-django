# Generated by Django 4.1.6 on 2024-03-28 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0008_alter_geogentities_name'),
        ('mdm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studies',
            name='organisation',
            field=models.ForeignKey(blank=True, db_column='organisation', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='studies_organisation', to='general.organisations'),
        ),
    ]
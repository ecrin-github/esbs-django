# Generated by Django 4.1.6 on 2023-04-09 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('context', '0002_alter_objecttypes_filter_as_and_more'),
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geogentities',
            name='geog_entity_type',
            field=models.ForeignKey(db_column='type_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geog_entities_type_id', to='context.geogentitytypes'),
        ),
        migrations.AlterField(
            model_name='geogentities',
            name='parent_id',
            field=models.ForeignKey(blank=True, db_column='parent_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geog_entities_parent_id', to='general.geogentities'),
        ),
        migrations.AlterField(
            model_name='orgattributes',
            name='attribute_type',
            field=models.ForeignKey(blank=True, db_column='attribute_type_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_attributes_attribute_type_id', to='context.orgattributetypes'),
        ),
        migrations.AlterField(
            model_name='orgattributes',
            name='organisation',
            field=models.ForeignKey(blank=True, db_column='organisation_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_attributes_org_id', to='general.organisations'),
        ),
        migrations.AlterField(
            model_name='orglinks',
            name='org_link_type',
            field=models.ForeignKey(blank=True, db_column='org_link_type_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_links_org_link_type', to='context.orglinktypes'),
        ),
        migrations.AlterField(
            model_name='orglinks',
            name='organisation',
            field=models.ForeignKey(blank=True, db_column='organisation_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_links_org_id', to='general.organisations'),
        ),
        migrations.AlterField(
            model_name='orglocations',
            name='city',
            field=models.ForeignKey(blank=True, db_column='city_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_locations_city_id', to='general.geogentities'),
        ),
        migrations.AlterField(
            model_name='orglocations',
            name='country',
            field=models.ForeignKey(blank=True, db_column='country_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_locations_country_id', to='general.geogentities'),
        ),
        migrations.AlterField(
            model_name='orglocations',
            name='organisation',
            field=models.ForeignKey(blank=True, db_column='organisation_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_locations_org_id', to='general.organisations'),
        ),
        migrations.AlterField(
            model_name='orgnames',
            name='changes_language',
            field=models.ForeignKey(blank=True, db_column='changes_language_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_names_changes_language', to='general.languagecodes'),
        ),
        migrations.AlterField(
            model_name='orgnames',
            name='lang_code',
            field=models.ForeignKey(blank=True, db_column='lang_code_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_names_lang_code_id', to='general.languagecodes'),
        ),
        migrations.AlterField(
            model_name='orgnames',
            name='organisation',
            field=models.ForeignKey(blank=True, db_column='organisation_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_names_org_id', to='general.organisations'),
        ),
        migrations.AlterField(
            model_name='orgnames',
            name='qualifier',
            field=models.ForeignKey(blank=True, db_column='qualifier_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_names_qualifier_id', to='context.orgnamequalifiertypes'),
        ),
        migrations.AlterField(
            model_name='orgrelationships',
            name='organisation',
            field=models.ForeignKey(blank=True, db_column='organisation_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_relationships_org_id', to='general.organisations'),
        ),
        migrations.AlterField(
            model_name='orgrelationships',
            name='relationship_type',
            field=models.ForeignKey(blank=True, db_column='relationship_type_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_relationships_relationship_type_id', to='context.orgrelationshiptypes'),
        ),
        migrations.AlterField(
            model_name='orgrelationships',
            name='target_org',
            field=models.ForeignKey(blank=True, db_column='target_org_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_relationships_target_org_id', to='general.organisations'),
        ),
        migrations.AlterField(
            model_name='orgtypemembership',
            name='org_type',
            field=models.ForeignKey(blank=True, db_column='org_type_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_type_membership_org_type_id', to='context.orgtypes'),
        ),
        migrations.AlterField(
            model_name='orgtypemembership',
            name='organisation',
            field=models.ForeignKey(blank=True, db_column='organisation_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_type_membership_org_id', to='general.organisations'),
        ),
    ]

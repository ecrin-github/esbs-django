# Generated by Django 4.1.6 on 2023-04-09 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('context', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objecttypes',
            name='filter_as',
            field=models.ForeignKey(blank=True, db_column='filter_as_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='object_types_filter_as_id', to='context.objectfiltertypes'),
        ),
        migrations.AlterField(
            model_name='objecttypes',
            name='object_class',
            field=models.ForeignKey(blank=True, db_column='object_class_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='object_types_object_class_id', to='context.objectclasses'),
        ),
        migrations.AlterField(
            model_name='orgattributetypes',
            name='org_attribute_datatype',
            field=models.ForeignKey(blank=True, db_column='org_attribute_datatype_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_attribute_types_org_attribute_datatype_id', to='context.orgattributedatatypes'),
        ),
        migrations.AlterField(
            model_name='orgattributetypes',
            name='parent_id',
            field=models.ForeignKey(blank=True, db_column='parent_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_attribute_types_parent_id', to='context.orgattributetypes'),
        ),
        migrations.AlterField(
            model_name='orgtypes',
            name='org_class',
            field=models.ForeignKey(blank=True, db_column='class_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_types_class_id', to='context.orgclasses'),
        ),
        migrations.AlterField(
            model_name='roletypes',
            name='role_class',
            field=models.ForeignKey(blank=True, db_column='role_class_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='role_types_role_class_id', to='context.roleclasses'),
        ),
        migrations.AlterField(
            model_name='studyfeaturecategories',
            name='feature_type',
            field=models.ForeignKey(blank=True, db_column='feature_type_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='study_feature_categories_feature_type_id', to='context.studyfeaturetypes'),
        ),
    ]

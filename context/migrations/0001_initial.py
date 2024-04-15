# Generated by Django 4.1.6 on 2024-04-08 15:44

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessPrereqTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(null=True)),
                ('created_on', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'access_prereq_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='CheckStatusTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(null=True)),
                ('created_on', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'check_status_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='CompositeHashTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('applies_to', models.CharField(db_index=True, max_length=75, null=True)),
                ('source', models.CharField(db_index=True, max_length=75, null=True)),
                ('description', models.TextField(null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'composite_hash_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='ContributorTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('applies_to', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
                ('use_in_data_entry', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'contributor_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='DatasetConsentTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField()),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'dataset_consent_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='DatasetDeidentificationLevels',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'dataset_deidentification_levels',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='DatasetRecordkeyTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'dataset_recordkey_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='DateTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('applies_to_papers_only', models.BooleanField(db_index=True, default=False)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
                ('use_in_data_entry', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'date_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='DescriptionTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
                ('use_in_data_entry', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'description_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='DoiStatusTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'doi_status_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='DtpStatusTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_on', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'dtp_status_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='DupStatusTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_on', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'dup_status_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='GenderEligibilityTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
                ('use_in_data_entry', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'gender_eligibility_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='GeogEntityTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'geog_entity_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='IdentifierTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('applies_to', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
                ('use_in_data_entry', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'identifier_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='LanguageUsageTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'language_usage_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='LegalStatusTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_on', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'legal_status_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='LinkTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'link_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='ObjectAccessTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
                ('use_in_data_entry', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'object_access_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='ObjectClasses',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
                ('use_in_data_entry', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'object_classes',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='ObjectFilterTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('filter_as', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'object_filter_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='ObjectInstanceTypes',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'object_instance_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='ObjectRelationshipTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
                ('use_in_data_entry', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'object_relationship_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='OrgAttributeDatatypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'org_attribute_datatypes',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='OrgClasses',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'org_classes',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='OrgLinkTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_on', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'org_link_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='OrgNameQualifierTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'org_name_qualifier_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='OrgRelationshipTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'org_relationship_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='PrereqTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_on', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'prereq_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='RepoAccessTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_on', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'repo_access_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='ResourceTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
                ('use_in_data_entry', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'resource_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='RmsUserTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'rms_user_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='RoleClasses',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'role_classes',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='SizeUnits',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'size_units',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='StudyFeatureTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
                ('context', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'study_feature_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='StudyRelationshipTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
                ('use_in_data_entry', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'study_relationship_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='StudyStatuses',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
                ('use_in_data_entry', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'study_statuses',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='StudyTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
                ('use_in_data_entry', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'study_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='TimeUnits',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
                ('use_in_data_entry', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'time_units',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='TitleTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('applies_to', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
                ('use_in_data_entry', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'title_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='TopicTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
                ('use_in_data_entry', models.BooleanField(default=True)),
                ('value_type', models.CharField(db_index=True, max_length=150)),
            ],
            options={
                'db_table': 'topic_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='TopicVocabularies',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
                ('use_in_data_entry', models.BooleanField(default=True)),
                ('url', models.URLField(blank=True, null=True)),
            ],
            options={
                'db_table': 'topic_vocabularies',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='TrialRegistries',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'trial_registries',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='UserTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
            ],
            options={
                'db_table': 'user_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='StudyFeatureCategories',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
                ('feature_type', models.ForeignKey(blank=True, db_column='feature_type_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='study_feature_categories_feature_type_id', to='context.studyfeaturetypes')),
            ],
            options={
                'db_table': 'study_feature_categories',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='RoleTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('list_order', models.IntegerField(default=0, null=True)),
                ('role_class', models.ForeignKey(blank=True, db_column='role_class_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='role_types_role_class_id', to='context.roleclasses')),
            ],
            options={
                'db_table': 'role_types',
                'ordering': ['list_order'],
            },
        ),
        migrations.CreateModel(
            name='OrgTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('org_class', models.ForeignKey(blank=True, db_column='class_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_types_class_id', to='context.orgclasses')),
            ],
            options={
                'db_table': 'org_types',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='OrgAttributeTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('can_repeat', models.BooleanField(default=False)),
                ('is_public', models.BooleanField(default=False)),
                ('org_attribute_datatype', models.ForeignKey(blank=True, db_column='org_attribute_datatype_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_attribute_types_org_attribute_datatype_id', to='context.orgattributedatatypes')),
                ('parent_id', models.ForeignKey(blank=True, db_column='parent_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='org_attribute_types_parent_id', to='context.orgattributetypes')),
            ],
            options={
                'db_table': 'org_attribute_types',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ObjectTypes',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=75)),
                ('source', models.CharField(db_index=True, max_length=75)),
                ('description', models.TextField(blank=True, null=True)),
                ('date_added', models.DateField(default=datetime.date.today, null=True)),
                ('list_order', models.IntegerField(default=0, null=True)),
                ('use_in_data_entry', models.BooleanField(default=True)),
                ('filter_as', models.ForeignKey(blank=True, db_column='filter_as_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='object_types_filter_as_id', to='context.objectfiltertypes')),
                ('object_class', models.ForeignKey(blank=True, db_column='object_class_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='object_types_object_class_id', to='context.objectclasses')),
            ],
            options={
                'db_table': 'object_types',
                'ordering': ['list_order'],
            },
        ),
    ]

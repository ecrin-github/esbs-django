import datetime
import uuid

from django.db import models

from configs.context_db_settings import IS_CONTEXT_DB_CONSTRAINT
from configs.users_db_settings import IS_USERS_DB_CONSTRAINT
from context.models.dataset_consent_types import DatasetConsentTypes
from context.models.dataset_deidentification_levels import DatasetDeidentificationLevels
from context.models.dataset_recordkey_types import DatasetRecordkeyTypes
from mdm.models.data_object.data_objects import DataObjects
from users.models.users import Users


class ObjectDatasets(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4, db_index=True)
    object_id = models.ForeignKey(DataObjects, on_delete=models.CASCADE, db_column='object_id',
                                  related_name='object_datasets', default=None, null=True, blank=True)
    recordkey_type = models.ForeignKey(DatasetRecordkeyTypes, on_delete=models.CASCADE,
                                       db_column='recordkey_type_id', default=None, null=True, blank=True,
                                       related_name='object_datasets_recordkey_type_id',
                                       db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    recordkey_details = models.TextField(null=True, blank=True)
    deident_type = models.ForeignKey(DatasetDeidentificationLevels, on_delete=models.CASCADE,
                                     db_column='deident_type_id', default=None, null=True, blank=True,
                                     related_name='object_datasets_deident_type_id',
                                     db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    deident_direct = models.BooleanField(default=False)
    deident_hipaa = models.BooleanField(default=False)
    deident_dates = models.BooleanField(default=False)
    deident_kanon = models.BooleanField(default=False)
    deident_nonarr = models.BooleanField(default=False)
    deident_details = models.TextField(null=True, blank=True)
    consent_type = models.ForeignKey(DatasetConsentTypes, on_delete=models.CASCADE, db_column='consent_type_id',
                                     related_name='object_datasets_consent_type_id', default=None, null=True,
                                     blank=True, db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    consent_noncommercial = models.BooleanField(default=False)
    consent_geog_restrict = models.BooleanField(default=False)
    consent_research_type = models.BooleanField(default=False)
    consent_genetic_only = models.BooleanField(default=False)
    consent_no_methods = models.BooleanField(default=False)
    consent_details = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)
    last_edited_by = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='last_edited_by',
                                       related_name='object_datasets_last_edited_by', default=None, null=True,
                                       blank=True, db_constraint=IS_USERS_DB_CONSTRAINT)

    class Meta:
        db_table = "object_datasets"
        ordering = ['created_on']

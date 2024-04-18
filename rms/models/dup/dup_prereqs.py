import datetime
import uuid

from django.db import models

from configs.context_db_settings import IS_CONTEXT_DB_CONSTRAINT
from configs.mdm_db_settings import IS_MDM_DB_CONSTRAINT
from context.models.access_prereq_types import AccessPrereqTypes
from mdm.models.data_object.data_objects import DataObjects
from rms.models.dup.dups import DataUseProcesses


class DupPrereqs(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, null=False, db_index=True, default=uuid.uuid4)
    dup_id = models.ForeignKey(DataUseProcesses, on_delete=models.CASCADE, db_column='dup_id',
                               related_name='dup_prereqs_dup_id', default=None, null=True, blank=True)
    object_id = models.ForeignKey(DataObjects, on_delete=models.CASCADE, db_column='object_id',
                                  related_name='dup_prereqs_object_id', default=None, null=True, blank=True,
                                  db_constraint=IS_MDM_DB_CONSTRAINT)
    prereq_type = models.ForeignKey(AccessPrereqTypes, on_delete=models.CASCADE, db_column='prereq_id',
                                    related_name='dup_prereqs_prereq_id', default=None, null=True, blank=True,
                                    db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    prereq_notes = models.TextField(blank=True, null=True)
    prereq_met = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'dup_prereqs'
        ordering = ['created_on']

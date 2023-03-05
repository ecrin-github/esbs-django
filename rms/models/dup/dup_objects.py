import datetime
import uuid

from django.db import models

from context.models.access_prereq_types import AccessPrereqTypes
from mdm.models.data_object.data_objects import DataObjects
from rms.models.dup.dups import DataUseProcesses


class DupObjects(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, db_index=True, unique=True)
    dup_id = models.ForeignKey(DataUseProcesses, on_delete=models.CASCADE, db_index=True,
                               related_name='dup_objects_dup_id')
    object_id = models.ForeignKey(DataObjects, on_delete=models.CASCADE, db_index=True,
                                  related_name='dup_objects_object_id')
    access_type = models.ForeignKey(AccessPrereqTypes, on_delete=models.CASCADE, db_index=True,
                                    related_name='dup_objects_access_type_id')
    access_details = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'dup_objects'
        ordering = ['created_on']

import datetime
import uuid

from django.db import models

from configs.context_db_settings import IS_CONTEXT_DB_CONSTRAINT
from configs.mdm_db_settings import IS_MDM_DB_CONSTRAINT
from context.models.access_prereq_types import AccessPrereqTypes
from mdm.models.data_object.data_objects import DataObjects
from rms.models.dtp.dtps import DataTransferProcesses


class DtpPrereqs(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, db_index=True, default=uuid.uuid4)
    dtp_id = models.ForeignKey(DataTransferProcesses, on_delete=models.CASCADE, db_column='dtp_id',
                               related_name='dtp_prereqs_dtp_id', default=None, null=True, blank=True)
    object_id = models.ForeignKey(DataObjects, on_delete=models.CASCADE, db_column='object_id',
                                  related_name='dtp_prereqs_object_id', default=None, null=True, blank=True,
                                  db_constraint=IS_MDM_DB_CONSTRAINT)
    prereq_type = models.ForeignKey(AccessPrereqTypes, on_delete=models.CASCADE, db_column='prereq_type_id',
                                    related_name='dtp_prereqs_prereq_type_id', default=None, null=True, blank=True,
                                    db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    prereq_notes = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'dtp_prereqs'
        ordering = ['created_on']

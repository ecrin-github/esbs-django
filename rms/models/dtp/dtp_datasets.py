import datetime
import uuid

from django.db import models

from configs.context_db_settings import IS_CONTEXT_DB_CONSTRAINT
from configs.mdm_db_settings import IS_MDM_DB_CONSTRAINT
from configs.users_db_settings import IS_USERS_DB_CONSTRAINT
from context.models.check_status_types import CheckStatusTypes
from context.models.legal_status_types import LegalStatusTypes
from mdm.models.data_object.data_objects import DataObjects
from rms.models.dtp.dtps import DataTransferProcesses
from users.models.users import Users


class DtpDatasets(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4, db_index=True)
    dtp_id = models.ForeignKey(DataTransferProcesses, on_delete=models.CASCADE, db_column='dtp_id', blank=True,
                               null=True, related_name='dtp_datasets_dtp_id', default=None)
    object_id = models.ForeignKey(DataObjects, on_delete=models.CASCADE, db_column='object_id', blank=True,
                                  null=True, related_name='dtp_datasets_object_id', default=None,
                                  db_constraint=IS_MDM_DB_CONSTRAINT)
    legal_status = models.ForeignKey(LegalStatusTypes, on_delete=models.CASCADE, db_column='legal_status_id',
                                     blank=True, null=True, related_name='dtp_datasets_legal_status_id', default=None,
                                     db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    legal_status_text = models.TextField(blank=True, null=True)
    legal_status_path = models.TextField(blank=True, null=True)
    desc_md_check_status = models.ForeignKey(CheckStatusTypes, on_delete=models.CASCADE,
                                             db_column='desc_md_check_status_id', blank=True, null=True,
                                             related_name='dtp_datasets_desc_md_check_status_id', default=None,
                                             db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    desc_md_check_status_date = models.DateTimeField(blank=True, null=True, default=datetime.datetime.utcnow)
    desc_md_check_by = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='desc_md_check_by', blank=True,
                                         null=True, related_name='dtp_datasets_desc_md_check_by', default=None,
                                         db_constraint=IS_USERS_DB_CONSTRAINT)
    deident_check_status = models.ForeignKey(CheckStatusTypes, on_delete=models.CASCADE,
                                             db_column='deident_check_status_id', blank=True, null=True,
                                             related_name='dtp_datasets_deident_check_status_id', default=None,
                                             db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    deident_check_status_date = models.DateTimeField(blank=True, null=True, default=datetime.datetime.utcnow)
    deident_check_by = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='deident_check_by',
                                         blank=True, null=True, related_name='dtp_datasets_deident_check_by',
                                         default=None, db_constraint=IS_USERS_DB_CONSTRAINT)
    notes = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'dtp_datasets'
        ordering = ['created_on']

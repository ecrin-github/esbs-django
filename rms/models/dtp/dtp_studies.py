import datetime
import uuid

from django.db import models

from configs.context_db_settings import IS_CONTEXT_DB_CONSTRAINT
from configs.mdm_db_settings import IS_MDM_DB_CONSTRAINT
from configs.users_db_settings import IS_USERS_DB_CONSTRAINT
from context.models.check_status_types import CheckStatusTypes
from mdm.models.study.studies import Studies
from rms.models.dtp.dtps import DataTransferProcesses
from users.models.users import Users


class DtpStudies(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, db_index=True, default=uuid.uuid4)
    dtp_id = models.ForeignKey(DataTransferProcesses, on_delete=models.CASCADE, db_column='dtp_id',
                               related_name='dtp_studies_dtp_id', default=None, null=True, blank=True)
    study_id = models.ForeignKey(Studies, on_delete=models.CASCADE, db_column='study_id',
                                 related_name='dtp_studies_study_id', default=None, null=True, blank=True,
                                 db_constraint=IS_MDM_DB_CONSTRAINT)
    md_check_status = models.ForeignKey(CheckStatusTypes, on_delete=models.CASCADE, db_column='md_check_status_id',
                                        related_name='dtp_studies_md_check_status_id', default=None, null=True,
                                        blank=True, db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    md_check_date = models.DateTimeField(blank=True, null=True)
    md_check_by = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='md_check_by',
                                    related_name='dtp_studies_md_check_by', default=None, null=True, blank=True,
                                    db_constraint=IS_USERS_DB_CONSTRAINT)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'dtp_studies'
        ordering = ['created_on']

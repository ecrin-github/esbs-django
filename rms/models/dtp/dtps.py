import datetime
import uuid

from django.db import models

from configs.context_db_settings import IS_CONTEXT_DB_CONSTRAINT
from configs.general_db_settings import IS_GENERAL_DB_CONSTRAINT
from context.models.dtp_status_types import DtpStatusTypes
from general.models.organisations import Organisations


class DataTransferProcesses(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4, db_index=True)
    organisation = models.ForeignKey(Organisations, on_delete=models.CASCADE, db_column='organisation_id',
                                     related_name='dtp_org_id', default=None, null=True, blank=True,
                                     db_constraint=IS_GENERAL_DB_CONSTRAINT)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.ForeignKey(DtpStatusTypes, on_delete=models.CASCADE, db_column='status_id',
                               related_name='dtp_status_id', default=None, null=True, blank=True,
                               db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    initial_contact_date = models.DateTimeField(blank=True, null=True)
    set_up_complete_date = models.DateTimeField(blank=True, null=True)
    md_access_granted_date = models.DateTimeField(blank=True, null=True)
    md_complete_date = models.DateTimeField(blank=True, null=True)
    dta_agreed_date = models.DateTimeField(blank=True, null=True)
    upload_access_requested_date = models.DateTimeField(blank=True, null=True)
    upload_access_confirmed_date = models.DateTimeField(blank=True, null=True)
    upload_complete_date = models.DateTimeField(blank=True, null=True)
    qc_checks_complete_date = models.DateTimeField(blank=True, null=True)
    md_integrated_with_mdr_date = models.DateTimeField(blank=True, null=True)
    availability_requested_date = models.DateTimeField(blank=True, null=True)
    availability_confirmed_date = models.DateTimeField(blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'data_transfer_processes'
        ordering = ['created_on']

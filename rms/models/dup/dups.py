import datetime
import uuid

from django.db import models

from configs.context_db_settings import IS_CONTEXT_DB_CONSTRAINT
from configs.general_db_settings import IS_GENERAL_DB_CONSTRAINT
from context.models.dup_status_types import DupStatusTypes
from general.models.organisations import Organisations
from rms.models.dup.data_access_request import DataAccessRequest


class DataUseProcesses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    organisation = models.ForeignKey(Organisations, on_delete=models.SET_NULL, db_column='org_id',
                                     related_name='organisation', default=None, null=True, blank=True,
                                     db_constraint=IS_GENERAL_DB_CONSTRAINT)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.ForeignKey(DupStatusTypes, models.SET_NULL, db_column='status_id',
                               related_name='dup_status_id', default=None, null=True, blank=True,
                               db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    data_access_request = models.ForeignKey(DataAccessRequest, models.SET_NULL, db_column='data_access_request_id',
                                            related_name='dup_id', default=None, null=True, blank=True)
    request_decision_date = models.DateTimeField(blank=True, null=True)
    agreement_signed_date = models.DateTimeField(blank=True, null=True)
    data_access_available_from = models.DateTimeField(blank=True, null=True)
    data_access_available_until = models.DateTimeField(blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'data_use_processes'
        ordering = ['created_on']

import datetime
import uuid

from django.db import models

from context.models.dup_status_types import DupStatusTypes
from general.models.organisations import Organisations


class DataUseProcesses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    org_id = models.ForeignKey(Organisations, on_delete=models.CASCADE, db_column='org_id',
                               related_name='dup_org_id')
    display_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.ForeignKey(DupStatusTypes, models.DO_NOTHING, db_column='status_id',
                               related_name='dup_status_id')
    initial_contact_date = models.DateTimeField(blank=True, null=True)
    set_up_completed_date = models.DateTimeField(blank=True, null=True)
    prereqs_met_date = models.DateTimeField(blank=True, null=True)
    dua_agreed_date = models.DateTimeField(blank=True, null=True)
    availability_requested_date = models.DateTimeField(blank=True, null=True)
    availability_confirmed_date = models.DateTimeField(blank=True, null=True)
    access_confirmed_date = models.DateTimeField(blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'data_use_processes'
        ordering = ['created_on']

import datetime
import uuid

from django.db import models

from rms.models.dup.dups import DataUseProcesses


class DupSecondaryUse(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    dup_id = models.ForeignKey(DataUseProcesses, on_delete=models.CASCADE, db_column='dup_id', db_index=True,
                               related_name='dup_secondary_use_dup_id', default=None, null=True, blank=True)
    secondary_use_summary = models.TextField(blank=True, null=True)
    publication = models.TextField(blank=True, null=True)
    doi = models.TextField(blank=True, null=True)
    attribution_present = models.BooleanField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'dup_secondary_use'
        ordering = ['created_on']

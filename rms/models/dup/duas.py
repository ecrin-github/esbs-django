import datetime
import uuid

from django.db import models

from rms.models.dup.dups import DataUseProcesses


class DataUseAccesses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    dup_id = models.ForeignKey(DataUseProcesses, on_delete=models.CASCADE, db_index=True,
                               related_name='dua_dup_id')
    conforms_to_default = models.BooleanField(default=False, db_index=True)
    variations = models.TextField(blank=True, null=True)
    repo_is_proxy_provider = models.BooleanField(default=False, db_index=True)
    dua_file_path = models.TextField(blank=True, null=True)
    repo_signatory_1 = models.IntegerField(blank=True, null=True)
    repo_signatory_2 = models.IntegerField(blank=True, null=True)
    provider_signatory_1 = models.IntegerField(blank=True, null=True)
    provider_signatory_2 = models.IntegerField(blank=True, null=True)
    requester_signatory_1 = models.IntegerField(blank=True, null=True)
    requester_signatory_2 = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(db_index=True, default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'data_use_accesses'
        ordering = ['created_on']

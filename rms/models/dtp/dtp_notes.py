import datetime
import uuid

from django.db import models

from rms.models.dtp.dtps import DataTransferProcesses
from users.models.users import Users


class DtpNotes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    dtp_id = models.ForeignKey(DataTransferProcesses, on_delete=models.CASCADE, db_column='dtp_id', blank=True,
                               null=True, related_name='dtp_notes_dtp_id')
    text = models.TextField(blank=True, null=True)
    author = models.ForeignKey(Users, models.DO_NOTHING, db_column='author', blank=True, null=True,
                               related_name='dtp_notes_author')
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'dtp_notes'
        ordering = ['created_on']

import datetime
import uuid

from django.db import models

from configs.users_db_settings import IS_USERS_DB_CONSTRAINT
from rms.models.dup.dups import DataUseProcesses
from users.models.users import Users


class DupNotes(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, db_index=True, unique=True)
    dup_id = models.ForeignKey(DataUseProcesses, on_delete=models.CASCADE, db_index=True,
                               related_name='dup_notes_dup_id', default=None, null=True, blank=True, db_column='dup_id')
    text = models.TextField(blank=True, null=True)
    author = models.ForeignKey(Users, on_delete=models.CASCADE, db_index=True, related_name='dup_notes_author',
                               default=None, null=True, blank=True, db_column='author',
                               db_constraint=IS_USERS_DB_CONSTRAINT)
    created_on = models.DateTimeField(db_index=True, default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'dup_notes'
        ordering = ['-created_on']

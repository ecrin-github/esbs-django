import uuid

from django.db import models

from configs.users_db_settings import IS_USERS_DB_CONSTRAINT
from rms.models.dup.dups import DataUseProcesses
from rms.models.dup.dup_people import DupPeople


class DataUseAccess(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    dup_id = models.ForeignKey(DataUseProcesses, on_delete=models.CASCADE, db_index=True,
                               related_name='access_dup_id', default=None, null=True, blank=True, db_column='dup_id')
    author = models.ForeignKey(Users, on_delete=models.CASCADE, db_index=True, related_name='dup_notes_author',
                               default=None, null=True, blank=True, db_column='author',
                               db_constraint=IS_USERS_DB_CONSTRAINT)

    class Meta:
        db_table = 'data_use_accesses'
        ordering = ['created_on']

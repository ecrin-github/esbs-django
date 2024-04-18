import datetime
import uuid

from django.db import models

from configs.users_db_settings import IS_USERS_DB_CONSTRAINT
from rms.models.dup.dups import DataUseProcesses
from users.models.users import Users


class DupPeople(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    dup_id = models.ForeignKey(DataUseProcesses, on_delete=models.CASCADE, db_column='dup_id', blank=True, null=True,
                               related_name='dup_people_dup_id', default=None)
    person = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='person_id', blank=True, null=True,
                               related_name='dup_people_person_id', default=None, db_constraint=IS_USERS_DB_CONSTRAINT)
    notes = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'dup_people'
        ordering = ['created_on']

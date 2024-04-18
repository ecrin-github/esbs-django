import datetime
import uuid

from django.db import models

from configs.users_db_settings import IS_USERS_DB_CONSTRAINT
from rms.models.dtp.dtps import DataTransferProcesses
from users.models.users import Users


class DtpPeople(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, null=False, db_index=True, default=uuid.uuid4)
    dtp_id = models.ForeignKey(DataTransferProcesses, on_delete=models.CASCADE, db_column='dtp_id', null=False,
                               related_name='dtp_people_dtp_id', default=None)
    person = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='person_id', null=False,
                               related_name='dtp_people_person_id', default=None, db_constraint=IS_USERS_DB_CONSTRAINT)
    notes = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'dtp_people'
        ordering = ['created_on']

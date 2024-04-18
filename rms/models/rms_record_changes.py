import datetime
import uuid

from django.db import models

from configs.users_db_settings import IS_USERS_DB_CONSTRAINT
from users.models.users import Users


class RmsRecordChanges(models.Model):
    # Change Types
    INSERT = 'Insert'
    UPDATE = 'Update'
    DELETE = 'Delete'
    CHANGE_TYPES = (
        (INSERT, 'Insert'),
        (UPDATE, 'Update'),
        (DELETE, 'Delete'),
    )

    id = models.UUIDField(primary_key=True, editable=False, unique=True, db_index=True, default=uuid.uuid4)
    table_name = models.CharField(max_length=255, blank=True, null=True)
    change_type = models.CharField(max_length=15, choices=CHANGE_TYPES, blank=True, null=True)
    change_time = models.DateTimeField(default=datetime.datetime.utcnow)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True,
                                related_name='rms_record_changes_user_id', default=None, db_column='user_id',
                                db_constraint=IS_USERS_DB_CONSTRAINT)
    previous_value = models.TextField(blank=True, null=True)
    new_value = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'rms_record_changes'
        ordering = ['-change_time']

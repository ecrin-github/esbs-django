import datetime
import uuid

from django.db import models

from mdm.models.data_object.data_objects import DataObjects
from users.models.users import Users


class ObjectRights(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, db_index=True, default=uuid.uuid4)
    object_id = models.ForeignKey(DataObjects, on_delete=models.CASCADE, db_column='object_id',
                                  related_name='object_rights_object_id')
    rights_name = models.CharField(max_length=255, blank=True, null=True)
    rights_url = models.URLField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)
    last_edited_by = models.ForeignKey(Users, related_name='object_rights_last_edited_by', on_delete=models.CASCADE,
                                       blank=True, null=True)

    class Meta:
        db_table = 'object_rights'
        ordering = ['created_on']

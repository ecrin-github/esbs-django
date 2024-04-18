import uuid
import datetime

from django.db import models


class CheckStatusTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    name = models.CharField(max_length=75, null=False, db_index=True)
    description = models.TextField(null=True)
    created_on = models.DateField(default=datetime.date.today, null=True)
    list_order = models.IntegerField(default=0, null=True)

    class Meta:
        db_table = "check_status_types"
        ordering = ["list_order"]

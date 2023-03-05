import uuid
from datetime import datetime

from django.db import models


class ObjectFilterTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    filter_as = models.CharField(max_length=75, db_index=True, unique=True)
    source = models.CharField(max_length=75, db_index=True)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(default=datetime.utcnow)
    list_order = models.IntegerField(default=0)

    class Meta:
        db_table = "object_filter_types"
        ordering = ["list_order"]

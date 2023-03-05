import uuid
from datetime import datetime

from django.db import models


class UserTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    name = models.CharField(max_length=75, unique=True, db_index=True)
    source = models.CharField(max_length=75, db_index=True)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(default=datetime.utcnow)
    list_order = models.IntegerField(default=0)

    class Meta:
        db_table = "user_types"
        ordering = ["list_order"]

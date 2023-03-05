import uuid

from django.db import models


class RoleClasses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    name = models.CharField(max_length=75, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    list_order = models.IntegerField(default=0)

    class Meta:
        db_table = "role_classes"
        ordering = ["list_order"]

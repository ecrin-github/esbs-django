import uuid

from django.db import models


class LinkTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    name = models.CharField(max_length=75, db_index=True, unique=True)
    description = models.TextField(blank=True, null=True)
    list_order = models.IntegerField(default=0)

    class Meta:
        db_table = "link_types"
        ordering = ["list_order"]

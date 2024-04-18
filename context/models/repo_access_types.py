import uuid
import datetime

from django.db import models


class RepoAccessTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    name = models.CharField(max_length=75, db_index=True)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateField(default=datetime.date.today, null=True)
    list_order = models.IntegerField(default=0, null=True)

    class Meta:
        db_table = "repo_access_types"
        ordering = ["list_order"]

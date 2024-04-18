import uuid
import datetime

from django.db import models


class DtpStatusTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    name = models.CharField(max_length=75, db_index=True)
    description = models.TextField(null=True, blank=True)
    created_on = models.DateField(default=datetime.date.today, null=True)
    list_order = models.IntegerField(default=0, null=True)

    class Meta:
        db_table = "dtp_status_types"
        ordering = ["list_order"]

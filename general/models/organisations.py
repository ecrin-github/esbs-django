import uuid
import datetime

from django.db import models


class Organisations(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    default_name = models.CharField(max_length=255, null=False, db_index=True)
    ror_id = models.TextField(null=True, db_index=True)
    display_suffix = models.CharField(max_length=255, null=True, db_index=True)
    scope_id = models.IntegerField(null=True, db_index=True)
    scope_notes = models.TextField(blank=True, null=True)
    is_current = models.BooleanField(default=True, db_index=True)
    year_established = models.IntegerField(null=True, db_index=True)
    year_ceased = models.IntegerField(null=True, db_index=True)
    city = models.CharField(max_length=255, null=True, db_index=True)
    country_code = models.CharField(max_length=50, null=True, db_index=True)
    country_name = models.CharField(max_length=255, null=True, db_index=True)
    created_on = models.DateField(default=datetime.date.today)

    class Meta:
        db_table = "organisations"
        ordering = ["default_name"]

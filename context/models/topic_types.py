import uuid
import datetime

from django.db import models


class TopicTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    name = models.CharField(max_length=75, db_index=True)
    source = models.CharField(max_length=75, db_index=True)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateField(default=datetime.date.today, null=True)
    list_order = models.IntegerField(default=0, null=True)
    use_in_data_entry = models.BooleanField(default=True)
    value_type = models.CharField(max_length=150, db_index=True)

    class Meta:
        db_table = "topic_types"
        ordering = ["list_order"]

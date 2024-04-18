import uuid
import datetime

from django.db import models

from context.models.object_classes import ObjectClasses
from context.models.object_filter_types import ObjectFilterTypes


class ObjectTypes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    name = models.CharField(max_length=75, db_index=True)
    object_class = models.ForeignKey(ObjectClasses, on_delete=models.CASCADE, db_index=True,
                                     related_name='object_types_object_class_id', db_column='object_class_id',
                                     default=None, null=True, blank=True)
    filter_as = models.ForeignKey(ObjectFilterTypes, on_delete=models.CASCADE, db_index=True,
                                  related_name="object_types_filter_as_id", db_column='filter_as_id',
                                  default=None, null=True, blank=True)
    source = models.CharField(max_length=75, db_index=True)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateField(default=datetime.date.today, null=True)
    list_order = models.IntegerField(default=0, null=True)
    use_in_data_entry = models.BooleanField(default=True)

    class Meta:
        db_table = "object_types"
        ordering = ["list_order"]

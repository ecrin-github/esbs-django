import uuid
import datetime

from django.db import models

from context.models.study_feature_types import StudyFeatureTypes


class StudyFeatureCategories(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    name = models.CharField(max_length=75, db_index=True)
    source = models.CharField(max_length=75, db_index=True)
    description = models.TextField(blank=True, null=True)
    date_added = models.DateField(default=datetime.date.today, null=True)
    list_order = models.IntegerField(default=0, null=True)
    feature_type = models.ForeignKey(StudyFeatureTypes, on_delete=models.CASCADE, db_index=True,
                                     related_name="study_feature_categories_feature_type_id",
                                     default=None, null=True, blank=True, db_column='feature_type_id')

    class Meta:
        db_table = "study_feature_categories"
        ordering = ["list_order"]

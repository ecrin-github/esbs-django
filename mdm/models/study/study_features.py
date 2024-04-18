import datetime
import uuid

from django.db import models

from configs.context_db_settings import IS_CONTEXT_DB_CONSTRAINT
from configs.users_db_settings import IS_USERS_DB_CONSTRAINT
from context.models.study_feature_categories import StudyFeatureCategories
from context.models.study_feature_types import StudyFeatureTypes
from mdm.models.study.studies import Studies
from users.models.users import Users


class StudyFeatures(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    study_id = models.ForeignKey(Studies, on_delete=models.CASCADE, db_column='study_id',
                                 related_name='study_features', default=None, null=True, blank=True)
    feature_type = models.ForeignKey(StudyFeatureTypes, on_delete=models.CASCADE, db_column='feature_type_id',
                                     related_name='study_features_feature_type_id', default=None, null=True, blank=True,
                                     db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    feature_value = models.ForeignKey(StudyFeatureCategories, on_delete=models.CASCADE, db_column='feature_value_id',
                                      related_name='study_features_feature_value_id', default=None, null=True,
                                      blank=True, db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)
    last_edited_by = models.ForeignKey(Users, null=True, blank=True, on_delete=models.CASCADE,
                                       related_name='study_features_last_edited_by', default=None,
                                       db_constraint=IS_USERS_DB_CONSTRAINT)

    class Meta:
        db_table = 'study_features'
        ordering = ['created_on']

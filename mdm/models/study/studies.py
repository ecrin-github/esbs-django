import datetime
import uuid

from django.db import models

from configs.context_db_settings import IS_CONTEXT_DB_CONSTRAINT
from configs.general_db_settings import IS_GENERAL_DB_CONSTRAINT
from configs.users_db_settings import IS_USERS_DB_CONSTRAINT
from context.models.gender_eligibility_types import GenderEligibilityTypes
from context.models.study_statuses import StudyStatuses
from context.models.study_types import StudyTypes
from context.models.time_units import TimeUnits
from general.models.language_codes import LanguageCodes
from users.models.users import Users


class Studies(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4, db_index=True)
    sd_sid = models.CharField(max_length=255, blank=True, null=True, editable=True, unique=True)
    display_title = models.CharField(max_length=255, blank=True, null=True)
    title_lang_code = models.ForeignKey(LanguageCodes, on_delete=models.CASCADE, db_column='title_lang_code_id',
                                        blank=True, null=True, default=None, db_constraint=IS_GENERAL_DB_CONSTRAINT,
                                        related_name='studies_title_lang_code')
    brief_description = models.TextField(blank=True, null=True)
    data_sharing_statement = models.TextField(blank=True, null=True)
    study_start_year = models.IntegerField(blank=True, null=True)
    study_start_month = models.IntegerField(blank=True, null=True)
    study_type = models.ForeignKey(StudyTypes, on_delete=models.CASCADE, db_column='study_type_id',
                                   blank=True, null=True, default=None,
                                   related_name='studies_study_type_id', db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    study_status = models.ForeignKey(StudyStatuses, on_delete=models.CASCADE, db_column='study_status_id',
                                     blank=True, null=True, default=None,
                                     related_name='studies_study_status_id', db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    study_enrollment = models.CharField(max_length=255, blank=True, null=True)
    study_gender_elig = models.ForeignKey(GenderEligibilityTypes, on_delete=models.CASCADE,
                                          db_column='study_gender_elig_id', blank=True, null=True,
                                          related_name='studies_study_gender_elig_id', default=None,
                                          db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    min_age = models.IntegerField(blank=True, null=True)
    min_age_unit = models.ForeignKey(TimeUnits, on_delete=models.CASCADE, db_column='min_age_unit_id', blank=True,
                                     null=True, related_name='studies_min_age_unit_id', default=None,
                                     db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    max_age = models.IntegerField(blank=True, null=True)
    max_age_unit = models.ForeignKey(TimeUnits, on_delete=models.CASCADE, db_column='max_age_unit_id', blank=True,
                                     null=True, related_name='studies_max_age_unit_id', default=None,
                                     db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)
    last_edited_by = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True,
                                       db_column='last_edited_by',
                                       related_name='studies_last_edited_by', default=None,
                                       db_constraint=IS_USERS_DB_CONSTRAINT)

    class Meta:
        db_table = 'studies'
        ordering = ['created_on']

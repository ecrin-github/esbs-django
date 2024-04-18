import datetime
import uuid

from django.db import models

from configs.context_db_settings import IS_CONTEXT_DB_CONSTRAINT
from configs.general_db_settings import IS_GENERAL_DB_CONSTRAINT
from configs.users_db_settings import IS_USERS_DB_CONSTRAINT
from context.models.contributor_types import ContributorTypes
from general.models.organisations import Organisations
from mdm.models.study.studies import Studies
from users.models.users import Users


class StudyContributors(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True, unique=True)
    study_id = models.ForeignKey(Studies, on_delete=models.CASCADE, db_column='study_id',
                                 related_name='study_contributors', default=None, null=True, blank=True)
    contributor_type = models.ForeignKey(ContributorTypes, on_delete=models.CASCADE, db_column='contributor_type_id',
                                         related_name='study_contributors_contributor_type_id', default=None,
                                         null=True, blank=True, db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    is_individual = models.BooleanField(default=False)
    person = models.ForeignKey(Users, null=True, blank=True, on_delete=models.CASCADE, db_column='person_id',
                               related_name='study_contributors_person_id', default=None,
                               db_constraint=IS_USERS_DB_CONSTRAINT)
    organisation = models.ForeignKey(Organisations, null=True, blank=True, on_delete=models.CASCADE,
                                     db_column='organisation_id', default=None,
                                     related_name='study_contributors_organisation_id',
                                     db_constraint=IS_GENERAL_DB_CONSTRAINT)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)
    last_edited_by = models.ForeignKey(Users, null=True, blank=True, on_delete=models.CASCADE,
                                       db_column='last_edited_by', default=None,
                                       related_name='study_contributors_last_edited_by',
                                       db_constraint=IS_USERS_DB_CONSTRAINT)

    class Meta:
        db_table = 'study_contributors'
        ordering = ['created_on']

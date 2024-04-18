import uuid

from django.db import models

from configs.context_db_settings import IS_CONTEXT_DB_CONSTRAINT
from context.models.org_names_qualifier_types import OrgNameQualifierTypes
from general.models.language_codes import LanguageCodes
from general.models.organisations import Organisations


class OrgNames(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, db_index=True, unique=True)
    organisation = models.ForeignKey(Organisations, on_delete=models.CASCADE, db_index=True,
                                     related_name="org_names_org_id", default=None, null=True, blank=True,
                                     db_column='organisation_id')
    qualifier = models.ForeignKey(OrgNameQualifierTypes, on_delete=models.CASCADE, db_index=True,
                                  related_name="org_names_qualifier_id", default=None, null=True, blank=True,
                                  db_column='qualifier_id', db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    lang_code = models.ForeignKey(LanguageCodes, on_delete=models.CASCADE, db_index=True,
                                  related_name="org_names_lang_code_id", default=None, null=True, blank=True,
                                  db_column='lang_code_id')
    script_code = models.CharField(max_length=255, db_index=True)
    changes_language = models.ForeignKey(LanguageCodes, on_delete=models.CASCADE, db_index=True,
                                         related_name="org_names_changes_language", default=None, null=True, blank=True,
                                         db_column='changes_language_id')
    name = models.CharField(max_length=255, db_index=True)

    class Meta:
        db_table = 'org_names'

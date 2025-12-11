import os
import random
import string
import uuid

from django.db import models

from general.models.organisations import Organisations
from mdm.models.study.studies import Studies
from users.models.users import Users


def get_cv_path(instance, filename):
    filename, file_extension = os.path.splitext(filename)
    return "uploads/CV_{0}{1}".format(''.join(random.choices(string.ascii_uppercase + string.digits, k=10)), file_extension)


class DataAccessRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    organisation = models.ForeignKey(Organisations, on_delete=models.SET_NULL, db_column='organisation_id',
                                     related_name='data_access_requests', default=None, null=True, blank=True)
    organisation_address = models.TextField(blank=True, null=True)
    principal_secondary_user = models.ForeignKey(Users, on_delete=models.SET_NULL, db_index=True, related_name='data_access_requests',
                                                 default=None, null=True, blank=True, db_column='secondary_user_id')
    cv = models.FileField(blank=True, null=True, upload_to=get_cv_path)
    additional_secondary_users = models.ManyToManyField(Users, blank=True)
    requested_study = models.ForeignKey(Studies, on_delete=models.SET_NULL, db_column='requested_study_id', # For now only 1 study requested
                                        related_name='data_access_requests', default=None, null=True, blank=True)
    project_title = models.CharField(max_length=1000, blank=True, null=True, db_index=True)
    project_type = models.CharField(max_length=1000, blank=True, null=True, db_index=True)
    project_abstract = models.TextField(blank=True, null=True)
    ethics_approval = models.CharField(max_length=30, blank=True, null=True)
    ethics_approval_details = models.CharField(max_length=1000, blank=True, null=True)
    project_funding = models.CharField(max_length=1000, blank=True, null=True)
    estimated_access_duration_required = models.CharField(max_length=255, blank=True, null=True)
    provisional_starting_date = models.DateField(blank=True, null=True)
    other_info = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'data_access_requests'
        ordering = ['id']

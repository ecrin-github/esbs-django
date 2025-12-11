import datetime
import uuid

from django.db import models

from configs.context_db_settings import IS_CONTEXT_DB_CONSTRAINT
from configs.mdm_db_settings import IS_MDM_DB_CONSTRAINT
from configs.rms_db_settings import IS_RMS_DB_CONSTRAINT
from context.models.check_status_types import CheckStatusTypes
from context.models.object_access_types import ObjectAccessTypes
from mdm.models.data_object.data_objects import DataObjects
from rms.models.dtp.dtps import DataTransferProcesses
from rms.models.dtp.dtp_people import DtpPeople
from rms.models.dtp.dtp_studies import DtpStudies


class DtpObjects(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, db_index=True)
    dtp_id = models.ForeignKey(DataTransferProcesses, on_delete=models.CASCADE, db_column='dtp_id', blank=True,
                               null=True, related_name='dtp_objects', default='')
    data_object = models.ForeignKey(DataObjects, on_delete=models.CASCADE, db_column='object_id', blank=True,
                                  null=True, related_name='dtp_objects', default='',
                                  db_constraint=IS_MDM_DB_CONSTRAINT)
    dtp_study = models.ForeignKey(DtpStudies, on_delete=models.CASCADE, db_index=True, related_name='dtp_objects', 
                                default=None, null=True, blank=True, db_column='dtp_study_id')
    is_dataset = models.BooleanField(default=False)
    access_type = models.ForeignKey(ObjectAccessTypes, on_delete=models.SET_DEFAULT, db_column='access_type_id',
                                    blank=True, null=True, related_name='dtp_objects', default='',
                                    db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    download_allowed = models.BooleanField(default=False)
    access_details = models.TextField(blank=True, null=True)
    embargo_requested = models.BooleanField(default=False)
    embargo_regime = models.TextField(blank=True, null=True)
    embargo_still_applies = models.BooleanField(default=False)
    access_check_status = models.ForeignKey(CheckStatusTypes, on_delete=models.SET_DEFAULT,
                                            db_column='access_check_status_id', blank=True, null=True,
                                            related_name='dtp_objects', default=None,
                                            db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    access_check_date = models.DateTimeField(blank=True, null=True)
    access_check_by = models.ForeignKey(DtpPeople, on_delete=models.SET_DEFAULT, db_column='access_check_by', blank=True,
                                        null=True, related_name='dtp_objects', default=None,
                                        db_constraint=IS_RMS_DB_CONSTRAINT)
    md_check_status = models.ForeignKey(CheckStatusTypes, on_delete=models.SET_DEFAULT, db_column='md_check_status_id',
                                        blank=True, null=True, related_name='dtp_objects_md_check',
                                        default=None, db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    md_check_date = models.DateTimeField(blank=True, null=True)
    md_check_by = models.ForeignKey(DtpPeople, on_delete=models.SET_DEFAULT, db_column='md_check_by', blank=True, null=True,
                                    related_name='dtp_objects_md_check', default=None,
                                    db_constraint=IS_RMS_DB_CONSTRAINT)
    notes = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'dtp_objects'
        ordering = ['created_on']

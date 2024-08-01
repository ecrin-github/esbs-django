import datetime
import uuid

from django.db import models

from configs.context_db_settings import IS_CONTEXT_DB_CONSTRAINT
from configs.general_db_settings import IS_GENERAL_DB_CONSTRAINT
from configs.users_db_settings import IS_USERS_DB_CONSTRAINT
from context.models.object_instance_types import ObjectInstanceTypes
from context.models.resource_types import ResourceTypes
from context.models.size_units import SizeUnits
from general.models.organisations import Organisations
from mdm.models.data_object.data_objects import DataObjects
from users.models.users import Users


class ObjectInstances(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, db_index=True, default=uuid.uuid4)
    sd_iid = models.CharField(max_length=255, blank=True, null=True)
    data_object = models.ForeignKey(DataObjects, on_delete=models.CASCADE, db_column='object_id',
                                  related_name='object_instances', default=None, null=True, blank=True)
    instance_type = models.ForeignKey(ObjectInstanceTypes, on_delete=models.CASCADE, db_index=True,
                                      related_name='object_instances_instance_type_id', default=None, null=True,
                                      blank=True, db_column='instance_type_id', db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    repository = models.CharField(max_length=200, db_index=True, null=True, blank=True)
    url = models.URLField(max_length=2000, null=True, blank=True)
    url_accessible = models.BooleanField(default=False, null=True, blank=True)
    url_last_checked = models.DateTimeField(null=True, blank=True)
    resource_type = models.ForeignKey(ResourceTypes, on_delete=models.CASCADE, db_index=True,
                                      related_name='object_instances_resource_type_id', default=None, null=True,
                                      blank=True, db_column='resource_type_id', db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    resource_size = models.BigIntegerField(null=True, blank=True)
    resource_size_unit = models.ForeignKey(SizeUnits, on_delete=models.CASCADE, db_index=True,
                                           related_name='object_instances_resource_size_unit_id', default=None,
                                           null=True, blank=True, db_column='resource_size_unit_id',
                                           db_constraint=IS_CONTEXT_DB_CONSTRAINT)
    resource_comments = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(default=datetime.datetime.utcnow)
    last_edited_by = models.ForeignKey(Users, on_delete=models.CASCADE, db_index=True,
                                       related_name='object_instances_last_edited_by', default=None, null=True,
                                       blank=True, db_column='last_edited_by', db_constraint=IS_USERS_DB_CONSTRAINT)

    class Meta:
        db_table = 'object_instances'
        ordering = ['created_on']

    def save(self, *args, **kwargs):
        if self._state.adding:
            # On insert - build instance ID
            data_object = DataObjects.objects.get(id=self.data_object.id)
            self.sd_iid = f'DSRI-{data_object.sd_oid[5:]}.{data_object.total_instances+1}'
            data_object.total_instances = models.F("total_instances") + 1
            data_object.save()
            data_object.refresh_from_db()
        super(ObjectInstances, self).save(*args, **kwargs)
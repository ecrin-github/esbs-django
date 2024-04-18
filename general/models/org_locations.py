import datetime
import uuid

from django.db import models

from general.models.geog_entities import GeogEntities
from general.models.organisations import Organisations


class OrgLocations(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True, db_index=True)
    organisation = models.ForeignKey(Organisations, on_delete=models.CASCADE, db_index=True,
                                     related_name="org_locations_org_id", default=None, null=True, blank=True,
                                     db_column='organisation_id')
    city = models.ForeignKey(GeogEntities, on_delete=models.CASCADE, blank=True, null=True, db_index=True,
                             related_name="org_locations_city_id", default=None, db_column='city_id')
    country = models.ForeignKey(GeogEntities, on_delete=models.CASCADE, blank=True, null=True, db_index=True,
                                related_name="org_locations_country_id", db_column='country_id', default=None)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True, db_index=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True, db_index=True)
    created_on = models.DateTimeField(db_index=True, default=datetime.datetime.utcnow)

    class Meta:
        db_table = 'org_locations'

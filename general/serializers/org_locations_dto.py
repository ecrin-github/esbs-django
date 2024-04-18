from rest_framework import serializers

from general.models.org_locations import OrgLocations
from general.serializers.geog_entities_dto import GeogEntitiesOutputSerializer
from general.serializers.organisations_dto import OrganisationsOutputSerializer


class OrgLocationsInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgLocations
        fields = '__all__'


class OrgLocationsOutputSerializer(serializers.ModelSerializer):
    organisation = OrganisationsOutputSerializer(many=False, read_only=True)
    city = GeogEntitiesOutputSerializer(many=False, read_only=True)
    country = GeogEntitiesOutputSerializer(many=False, read_only=True)

    class Meta:
        model = OrgLocations
        fields = '__all__'

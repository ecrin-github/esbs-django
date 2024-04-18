from rest_framework import serializers

from general.models.organisations import Organisations


class OrganisationsInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisations
        fields = '__all__'


class OrganisationsOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisations
        fields = '__all__'

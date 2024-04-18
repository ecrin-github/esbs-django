from rest_framework import serializers

from general.models.mesh_lookup import MeshLookup


class MeshLookupInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeshLookup
        fields = '__all__'


class MeshLookupOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeshLookup
        fields = '__all__'

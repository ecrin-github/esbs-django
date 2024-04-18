from rest_framework import serializers

from context.serializers.identifier_types_dto import IdentifierTypesOutputSerializer
from general.serializers.organisations_dto import OrganisationsOutputSerializer
from mdm.models.data_object.object_identifiers import ObjectIdentifiers
from users.models import Users
from users.serializers.users_dto import UsersSerializer


class ObjectIdentifiersInputSerializer(serializers.ModelSerializer):
    last_edited_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=Users.objects.all()
    )

    class Meta:
        model = ObjectIdentifiers
        fields = '__all__'


class ObjectIdentifiersOutputSerializer(serializers.ModelSerializer):
    identifier_type = IdentifierTypesOutputSerializer(many=False, read_only=True)
    identifier_org = OrganisationsOutputSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = ObjectIdentifiers
        fields = '__all__'

from rest_framework import serializers

from context.serializers.object_relationship_types_dto import ObjectRelationshipTypesOutputSerializer
from mdm.models.data_object.object_relationships import ObjectRelationships
from users.models import Users
from users.serializers.users_dto import UsersSerializer


class ObjectRelationshipsInputSerializer(serializers.ModelSerializer):
    last_edited_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=Users.objects.all()
    )

    class Meta:
        model = ObjectRelationships
        fields = '__all__'


class ObjectRelationshipsOutputSerializer(serializers.ModelSerializer):
    relationship_type = ObjectRelationshipTypesOutputSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = ObjectRelationships
        fields = '__all__'

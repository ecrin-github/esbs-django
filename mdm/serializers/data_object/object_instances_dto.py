from rest_framework import serializers

from context.serializers.object_instance_types_dto import ObjectInstanceTypesOutputSerializer
from context.serializers.resource_types_dto import ResourceTypesOutputSerializer
from context.serializers.size_units_dto import SizeUnitsOutputSerializer
from general.serializers.organisations_dto import OrganisationsOutputSerializer
from mdm.models.data_object.data_objects import DataObjects
from mdm.models.data_object.object_instances import ObjectInstances
from users.models import Users
from users.serializers.users_dto import UsersSerializer


class ObjectInstancesInputSerializerCreate(serializers.ModelSerializer):
    last_edited_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=Users.objects.all()
    )

    class Meta:
        model = ObjectInstances
        fields = '__all__'


class ObjectInstancesInputSerializerUpdate(serializers.ModelSerializer):
    last_edited_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=Users.objects.all()
    )

    class Meta:
        model = ObjectInstances
        # Not updating sd_iid
        exclude = ['sd_iid']


class ObjectInstancesOutputSerializer(serializers.ModelSerializer):
    instance_type = ObjectInstanceTypesOutputSerializer(many=False, read_only=True)
    resource_type = ResourceTypesOutputSerializer(many=False, read_only=True)
    resource_size_unit = SizeUnitsOutputSerializer(many=False, read_only=True)
    # last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = ObjectInstances
        # fields = '__all__'
        exclude = ['last_edited_by']


class ObjectInstancesLimitedOutputSerializer(serializers.ModelSerializer):
    instance_type = ObjectInstanceTypesOutputSerializer(many=False, read_only=True)
    resource_type = ResourceTypesOutputSerializer(many=False, read_only=True)
    resource_size_unit = SizeUnitsOutputSerializer(many=False, read_only=True)
    url = serializers.SerializerMethodField()
    # last_edited_by = UsersSerializer(many=False, read_only=True)

    def get_url(self, obj):
        return '[hidden]' if obj.url != '' else obj.url

    class Meta:
        model = ObjectInstances
        # fields = '__all__'
        exclude = ['last_edited_by']
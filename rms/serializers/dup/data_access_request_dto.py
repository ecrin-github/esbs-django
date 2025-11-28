from rest_framework import serializers

from rms.models.dup.data_access_request import DataAccessRequest
from users.models.users import Users
from general.serializers.organisations_dto import OrganisationsInputSerializer, OrganisationsOutputSerializer
from mdm.serializers.study.studies_dto import StudiesLimitedOutputSerializer
from users.serializers.users_dto import UsersSerializer, UsersLimitedSerializer


class DataAccessRequestInputSerializer(serializers.ModelSerializer):
    additional_secondary_users = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Users.objects.all(), required=False, allow_null=True)

    class Meta:
        model = DataAccessRequest
        fields = '__all__'


class DataAccessRequestOutputSerializer(serializers.ModelSerializer):
    organisation = OrganisationsOutputSerializer(many=False, read_only=True)
    principal_secondary_user = UsersLimitedSerializer(many=False, read_only=True)
    additional_secondary_users = UsersLimitedSerializer(many=True, read_only=True)
    requested_study = StudiesLimitedOutputSerializer(many=False, read_only=True)

    class Meta:
        model = DataAccessRequest
        fields = '__all__'


class DataAccessRequestReconstructSerializer(serializers.ModelSerializer):
    organisation = OrganisationsInputSerializer(many=False, read_only=True)
    principal_secondary_user = UsersSerializer(many=True, read_only=True)
    additional_secondary_users = UsersSerializer(many=True, read_only=True, required=False, allow_null=True)

    class Meta:
        model = DataAccessRequest
        fields = '__all__'
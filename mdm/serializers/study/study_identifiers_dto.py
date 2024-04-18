from rest_framework import serializers

from context.serializers.identifier_types_dto import IdentifierTypesOutputSerializer
from general.serializers.organisations_dto import OrganisationsOutputSerializer
from mdm.models.study.study_identifiers import StudyIdentifiers
from users.models import Users
from users.serializers.users_dto import UsersSerializer


class StudyIdentifiersInputSerializer(serializers.ModelSerializer):
    last_edited_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=Users.objects.all()
    )

    class Meta:
        model = StudyIdentifiers
        fields = '__all__'


class StudyIdentifiersOutputSerializer(serializers.ModelSerializer):
    identifier_type = IdentifierTypesOutputSerializer(many=False, read_only=True)
    identifier_org = OrganisationsOutputSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = StudyIdentifiers
        fields = '__all__'

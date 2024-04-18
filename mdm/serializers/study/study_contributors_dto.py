from rest_framework import serializers

from context.serializers.contributor_types_dto import ContributorTypesOutputSerializer
from general.serializers.organisations_dto import OrganisationsOutputSerializer
from mdm.models.study.study_contributors import StudyContributors
from users.models import Users
from users.serializers.users_dto import UsersSerializer


class StudyContributorsInputSerializer(serializers.ModelSerializer):
    last_edited_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=Users.objects.all()
    )

    class Meta:
        model = StudyContributors
        fields = '__all__'


class StudyContributorsOutputSerializer(serializers.ModelSerializer):
    contributor_type = ContributorTypesOutputSerializer(many=False, read_only=True)
    person = UsersSerializer(many=False, read_only=True)
    organisation = OrganisationsOutputSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = StudyContributors
        fields = '__all__'

from rest_framework import serializers

from context.serializers.contributor_types_dto import ContributorTypesOutputSerializer
from general.serializers.organisations_dto import OrganisationsOutputSerializer
from mdm.models.data_object.object_contributors import ObjectContributors
from users.models import Users
from users.serializers.users_dto import UsersSerializer


class ObjectContributorsInputSerializer(serializers.ModelSerializer):
    last_edited_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=Users.objects.all()
    )

    class Meta:
        model = ObjectContributors
        fields = '__all__'


class ObjectContributorsOutputSerializer(serializers.ModelSerializer):
    contributor_type = ContributorTypesOutputSerializer(many=False, read_only=True)
    person = UsersSerializer(many=False, read_only=True)
    organisation = OrganisationsOutputSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = ObjectContributors
        fields = '__all__'

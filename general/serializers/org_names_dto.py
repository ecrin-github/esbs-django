from rest_framework import serializers

from context.serializers.org_names_qualifier_types_dto import OrgNameQualifierTypesOutputSerializer
from general.models.org_names import OrgNames
from general.serializers.language_codes_dto import LanguageCodesOutputSerializer
from general.serializers.organisations_dto import OrganisationsOutputSerializer


class OrgNamesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgNames
        fields = '__all__'


class OrgNamesOutputSerializer(serializers.ModelSerializer):
    organisation = OrganisationsOutputSerializer(many=False, read_only=True)
    qualifier = OrgNameQualifierTypesOutputSerializer(many=False, read_only=True)
    lang_code = LanguageCodesOutputSerializer(many=False, read_only=True)
    changes_language = LanguageCodesOutputSerializer(many=False, read_only=True)

    class Meta:
        model = OrgNames
        fields = '__all__'

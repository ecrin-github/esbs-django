from rest_framework import serializers

from context.serializers.dup_status_types_dto import DupStatusTypesOutputSerializer
from general.serializers.organisations_dto import OrganisationsOutputSerializer
from rms.serializers.dup.data_access_request_dto import DataAccessRequestOutputSerializer
from rms.serializers.dup.dup_objects_dto import DupObjectsOutputSerializer
from rms.serializers.dup.dup_people_dto import DupPeopleOutputSerializer
from rms.serializers.dup.dup_studies_dto import DupStudiesOutputSerializer
from rms.models.dup.dups import DataUseProcesses


class DataUseProcessesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataUseProcesses
        fields = '__all__'


class DataUseProcessesOutputSerializer(serializers.ModelSerializer):
    status = DupStatusTypesOutputSerializer(many=False, read_only=True)
    organisation = OrganisationsOutputSerializer(many=False, read_only=True)
    data_access_request = DataAccessRequestOutputSerializer(many=False, read_only=True)
    dup_objects = DupObjectsOutputSerializer(many=True, read_only=True)
    dup_studies = DupStudiesOutputSerializer(many=True, read_only=True)
    dup_people = DupPeopleOutputSerializer(many=True, read_only=True)

    class Meta:
        model = DataUseProcesses
        fields = '__all__'

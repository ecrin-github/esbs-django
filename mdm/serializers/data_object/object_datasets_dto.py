from rest_framework import serializers

from context.serializers.dataset_consent_types_dto import DatasetConsentTypesOutputSerializer
from context.serializers.dataset_deidentification_levels_dto import DatasetDeidentificationLevelsOutputSerializer
from context.serializers.dataset_recordkey_types_dto import DatasetRecordkeyTypesOutputSerializer
from mdm.models.data_object.object_datasets import ObjectDatasets
from users.models import Users
from users.serializers.users_dto import UsersSerializer


class ObjectDatasetsInputSerializer(serializers.ModelSerializer):
    last_edited_by = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=Users.objects.all()
    )

    class Meta:
        model = ObjectDatasets
        fields = '__all__'


class ObjectDatasetsOutputSerializer(serializers.ModelSerializer):
    recordkey_type = DatasetRecordkeyTypesOutputSerializer(many=False, read_only=True)
    deident_type = DatasetDeidentificationLevelsOutputSerializer(many=False, read_only=True)
    consent_type = DatasetConsentTypesOutputSerializer(many=False, read_only=True)
    last_edited_by = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = ObjectDatasets
        fields = '__all__'

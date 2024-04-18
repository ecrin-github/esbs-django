from rest_framework import serializers

from context.models.dtp_status_types import DtpStatusTypes


class DtpStatusTypesInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DtpStatusTypes
        fields = '__all__'


class DtpStatusTypesOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = DtpStatusTypes
        fields = '__all__'

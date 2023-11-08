from django.core.mail import send_mail
from rest_framework import permissions

from rest_framework.response import Response
from rest_framework.views import APIView

from app.serializers import MailSerializer
from mdm.models import Studies, DataObjects
from rms.models import DataUseProcesses, DataTransferProcesses
from users.models import Users


class EmailSender(APIView):
    permission_classes = [permissions.AllowAny]
    def get_serializer(self, *args, **kwargs):
        return MailSerializer(*args, **kwargs)

    def post(self, request, format=None):
        serializer = MailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success'}, status=200)
        return Response(serializer.errors,  status=400)


class RmsStatistics(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response({
            "total_studies": Studies.objects.all().count(),
            "total_objects": DataObjects.objects.all().count(),
            "dup": {
                "total": DataUseProcesses.objects.all().count(),
                "completed": DataUseProcesses.objects.filter(status__name='Complete').count()
            },
            "dtp": {
                "total": DataTransferProcesses.objects.all().count(),
                "completed": DataTransferProcesses.objects.filter(status__name='Complete').count()
            },
            "total_users": Users.objects.all().count()
        })


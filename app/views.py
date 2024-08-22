import time
from asgiref.sync import async_to_sync, sync_to_async
from channels.layers import get_channel_layer
from rest_framework import permissions, status
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from app.permissions import IsSuperUser
from app.serializers import MailSerializer
from mdm.models import Studies, DataObjects
from rms.models import DataUseProcesses, DataTransferProcesses
from users.models import Users, Notifications

import logging


class EmailSender(APIView):
    permission_classes = [permissions.AllowAny]

    def get_serializer(self, *args, **kwargs):
        return MailSerializer(*args, **kwargs)

    def post(self, request, format=None):
        serializer = MailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success'}, status=200)
        return Response(serializer.errors, status=400)


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


class PushNotifications(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsSuperUser]

    def post(self, request):
        if "message" in request.POST:
            message = request.POST['message']
            if "target_users" in request.POST:
                target_users = request.POST['target_users']
                user_ids = target_users.split(",")
                channel_layer = get_channel_layer()
                for uid in user_ids:
                    user = Users.objects.get(id=uid)
                    if user.online > 0:
                        # Send notification immediately if user is online
                        async_to_sync(channel_layer.group_send)(
                            f"push_notifications_{uid.strip()}",
                            {
                                "type": "send.notification",
                                "time": time.time(),
                                "message": message,
                            },
                        )
                    else:
                        # Store message to display for next connection
                        Notifications.objects.create(user=user, message=message)
                        
                return Response(status=status.HTTP_201_CREATED, data="Message sent")
            return Response(status=400, data="Target users to send notifications to are missing")
        return Response(status=400, data="Message to send to users is missing")

from mozilla_django_oidc.contrib.drf import OIDCAuthentication
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.views import APIView

from general.models import Organisations
from mdm.models import Studies, DataObjects
from rms.models import DataUseProcesses, DataTransferProcesses, DupStudies, DupObjects, DtpStudies, DtpObjects
from users.models.profiles import UserProfiles
from users.models.users import Users
from users.serializers.profiles_dto import UserProfilesOutputSerializer
from users.serializers.users_dto import UsersSerializer, CreateUserSerializer

from rest_framework.response import Response


class UsersList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action in ["create"]:
            return CreateUserSerializer
        return super().get_serializer_class()


class UserProfilesList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = UserProfiles.objects.all()
    serializer_class = UserProfilesOutputSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(user=self.kwargs['userId'])
        )


class UserEntitiesApiView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, userId, format=None):
        # user_id = request.query_params["userId"]
        # user_id = request.user.id

        user = Users.objects.filter(id=userId)
        if not user.exists():
            return Response(status=404, data="User not found")

        user_profile = UserProfiles.objects.filter(user_id=userId)
        if not user_profile.exists():
            return Response(status=404, data="User profile not found")

        org_id = user_profile[0].organisation_id
        organisation = Organisations.objects.get(id=org_id)

        dups = DataUseProcesses.objects.filter(org_id=organisation)
        dtps = DataTransferProcesses.objects.filter(organisation=organisation)

        study_id_list = []
        data_object_id_list = []

        for dup in dups:
            dup_studies = DupStudies.objects.filter(dup_id=dup)
            for dup_study_obj in dup_studies:
                study_id_list.append(dup_study_obj.study_id)

            dup_data_objects = DupObjects.objects.filter(dup_id=dup)
            for dup_data_object_obj in dup_data_objects:
                data_object_id_list.append(dup_data_object_obj.object_id)

        for dtp in dtps:
            dtp_studies = DtpStudies.objects.filter(dtp_id=dtp)
            for dtp_study_obj in dtp_studies:
                study_id_list.append(dtp_study_obj.study_id)
            dtp_data_objects = DtpObjects.objects.filter(dtp_id=dtp)
            for dtp_data_object_obj in dtp_data_objects:
                data_object_id_list.append(dtp_data_object_obj.object_id)

        studies_id_set = set(study_id_list)
        data_objects_id_set = set(data_object_id_list)

        studies = Studies.objects.filter(id__in=studies_id_set)
        data_objects = DataObjects.objects.filter(id__in=data_objects_id_set)

        data = {
            "studies": studies,
            "data_objects": data_objects,
            "dups": dups,
            "dtps": dtps
        }

        return Response(data,  status=200)

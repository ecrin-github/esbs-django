from mozilla_django_oidc.contrib.drf import OIDCAuthentication
from rest_framework import viewsets, permissions, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView

from general.models import Organisations
from mdm.models import Studies, DataObjects
from rms.models import DataUseProcesses, DataTransferProcesses, DupStudies, DupObjects, DtpStudies, DtpObjects
from users.models.profiles import UserProfiles
from users.models.users import Users
from users.serializers.profiles_dto import UserProfilesOutputSerializer, UserProfilesInputSerializer
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

    def create(self, request, *args, **kwargs):
        input_serializer = self.get_serializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        self.perform_create(input_serializer)

        user = Users.objects.get(email=input_serializer.validated_data["email"])
        output_serializer = UsersSerializer(user)
        return Response(output_serializer.data)


    def perform_create(self, serializer):
        family_name_val = self.request.data.get("family_name")
        serializer.save()


class UserProfilesList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = UserProfiles.objects.all()
    serializer_class = UserProfilesOutputSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return UserProfilesInputSerializer
        return super().get_serializer_class()

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


class UsersByOrganisation(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        org_id = self.request.query_params.get('orgId')

        if org_id is None:
            return Response({'error': "orgId param is missing"})

        organisation = Organisations.objects.get(id=org_id)

        users = Users.objects.filter(user_profile__organisation=organisation)

        serializer = UsersSerializer(users, many=True)

        return Response({'count': users.count(), 'results': serializer.data, 'statusCode': status.HTTP_200_OK})

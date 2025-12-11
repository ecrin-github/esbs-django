import datetime

from django.db.models import Value, Q
from django.db.models.functions import Concat
from django.core.exceptions import BadRequest, ValidationError
from django.http import JsonResponse
from mozilla_django_oidc.contrib.drf import OIDCAuthentication
from rest_framework import viewsets, permissions, status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from app.permissions import IsSuperUser, WriteOnlyForSelf
from context.models import ObjectAccessTypes
from general.models import Organisations
from mdm.models import Studies, DataObjects, ObjectInstances
from mdm.serializers.study.studies_dto import StudyDUPSerializer
from rms.models import DataUseProcesses, DataTransferProcesses, DupStudies, DupObjects, DtpStudies, DtpObjects, DtpPeople, DupPeople
from users.models.profiles import UserProfiles
from users.models.users import Users
from users.serializers.profiles_dto import UserProfilesOutputSerializer, UserProfilesInputSerializer
from users.serializers.users_dto import UsersSerializer, CreateUserSerializer, UsersLimitedSerializer


DUP_STATUS_INDEX_ACCESS_GRANTED = 4
DTP_STATUS_INDEX_TRANSFER = 4


class UsersList(GenericAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = Users.objects.filter(~Q(username='tsd'))
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        serializer = None
        if "sub" in request.GET:
            sub = request.GET['sub']
            user_profile_check = UserProfiles.objects.filter(ls_aai_id=sub)
            if user_profile_check.exists():
                user_profile = UserProfiles.objects.get(ls_aai_id=sub)
                user_check = self.get_queryset(*args, **kwargs).filter(id=user_profile.user.id)
                if user_check.exists():
                    user = self.get_queryset(*args, **kwargs).get(id=user_profile.user.id)
                    serializer = UsersSerializer(user, many=False)
        elif request.user.id:
            users = []
            if request.user.is_superuser:
                users = self.get_queryset(*args, **kwargs)
                serializer = UsersSerializer(users, many=True)
            else:
                try:
                    # Unused
                    users_subquery = self.get_queryset(*args, **kwargs).raw("SELECT u.id as id FROM users u LEFT JOIN "
                                        + "user_profiles up ON u.id=up.user_id "
                                        + f"WHERE up.organisation_id='{request.user.user_profile.organisation.id}';")
                    for user in users_subquery:
                        users.append(user)
                except AttributeError:
                    return Response(status=404, data='Error: no organisation for user')
                serializer = UsersLimitedSerializer(users, many=True)

        if not serializer:
            return Response(status=404, data="Requesting user not found")
        return Response({'count': len(serializer.data), 'results': serializer.data, 'statusCode': status.HTTP_200_OK})


class UserView(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.IsAuthenticated & (WriteOnlyForSelf | IsSuperUser)]

    def get_serializer_class(self):
        if self.action in ["create"]:
            return CreateUserSerializer
        return super().get_serializer_class()

    def create(self, request, *args, **kwargs):
        try:
            input_serializer = self.get_serializer(data=request.data)
            input_serializer.is_valid(raise_exception=True)
            self.perform_create(input_serializer)

            user = Users.objects.get(email=input_serializer.validated_data["email"])
            output_serializer = UsersSerializer(user)
            return Response(output_serializer.data)
        except BadRequest as e:
            return JsonResponse({'statusCode': 400, 'message': 'User profile exists but cannot find associated user.'})

    def perform_create(self, serializer):
        serializer.save()


class UserProfilesList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = UserProfiles.objects.all()
    serializer_class = UserProfilesOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (WriteOnlyForSelf | IsSuperUser)]

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


# class UserEntitiesApiView(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request, userId, format=None):
#         # user_id = request.query_params["userId"]
#         # user_id = request.user.id

#         user = Users.objects.filter(id=userId)
#         if not user.exists():
#             return Response(status=404, data="User not found")

#         user_profile = UserProfiles.objects.filter(user_id=userId)
#         if not user_profile.exists():
#             return Response(status=404, data="User profile not found")

#         org_id = user_profile[0].organisation_id
#         organisation = Organisations.objects.get(id=org_id)

#         dups = DataUseProcesses.objects.filter(org_id=organisation)
#         dtps = DataTransferProcesses.objects.filter(organisation=organisation)

#         study_id_list = []
#         data_object_id_list = []

#         for dup in dups:
#             dup_studies = DupStudies.objects.filter(dup_id=dup)
#             for dup_study_obj in dup_studies:
#                 study_id_list.append(dup_study_obj.study_id)

#             dup_data_objects = DupObjects.objects.filter(dup_id=dup)
#             for dup_data_object_obj in dup_data_objects:
#                 data_object_id_list.append(dup_data_object_obj.object_id)

#         for dtp in dtps:
#             dtp_studies = DtpStudies.objects.filter(dtp_id=dtp)
#             for dtp_study_obj in dtp_studies:
#                 study_id_list.append(dtp_study_obj.study_id)
#             dtp_data_objects = DtpObjects.objects.filter(dtp_id=dtp)
#             for dtp_data_object_obj in dtp_data_objects:
#                 data_object_id_list.append(dtp_data_object_obj.object_id)

#         studies_id_set = set(study_id_list)
#         data_objects_id_set = set(data_object_id_list)

#         studies = Studies.objects.filter(id__in=studies_id_set)
#         data_objects = DataObjects.objects.filter(id__in=data_objects_id_set)

#         data = {
#             "studies": studies,
#             "data_objects": data_objects,
#             "dups": dups,
#             "dtps": dtps
#         }

#         return Response(data,  status=200)


class UsersByOrganisation(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [IsSuperUser]

    def get(self, request):
        org_id = self.request.query_params.get('orgId')

        if org_id is None:
            return Response({'error': "orgId param is missing"})

        organisation = Organisations.objects.get(id=org_id)

        users = Users.objects.filter(user_profile__organisation=organisation)

        serializer = UsersSerializer(users, many=True)

        return Response({'count': users.count(), 'results': serializer.data, 'statusCode': status.HTTP_200_OK})


class UsersByName(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [IsSuperUser]

    def get(self, request):
        name = self.request.query_params.get('name')

        if name is None:
            return Response({'error': "name param is missing"})

        queryset = Users.objects.annotate(fullname=Concat('first_name', Value(' '), 'last_name'))
        result = queryset.filter(Q(fullname__icontains=name) | Q(email__icontains=name))

        serializer = UsersSerializer(result, many=True)

        return Response({'count': result.count(), 'results': serializer.data, 'statusCode': status.HTTP_200_OK})


class UsersByNameAndOrganisation(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [IsSuperUser]

    def get(self, request):
        name = self.request.query_params.get('name')

        if name is None:
            return Response({'error': "name param is missing"})

        org_id = self.request.query_params.get('orgId')
        if org_id is None:
            return Response({'error': "orgId param is missing"})

        org_check = Organisations.objects.filter(id=org_id)
        if not org_check.exists():
            return Response({'error': f'Organisation with the ID {org_id} does not exist'})

        org_data = Organisations.objects.get(id=org_id)

        queryset = Users.objects.annotate(fullname=Concat('first_name', Value(' '), 'last_name'))
        result = queryset.filter(Q(fullname__icontains=name) | Q(email__icontains=name))
        res = result.filter(user_profile__organisation=org_data)

        serializer = UsersSerializer(res, many=True)

        return Response({'count': result.count(), 'results': serializer.data, 'statusCode': status.HTTP_200_OK})


# class UserByEmail(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request):
#         email = self.request.query_params.get('email')

#         if email is None:
#             return Response({'error': "email param is missing"})

#         user_check = Users.objects.filter(email=email)
#         if not user_check.exists():
#             return Response({'error': f'User with the Email {email} does not exist'})

#         user_data = Users.objects.get(email=email)

#         serializer = UsersSerializer(user_data)

#         return Response(serializer.data)


# class UserByLsAaiId(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request):
#         ls_aai_id = self.request.query_params.get('id')

#         if ls_aai_id is None:
#             return Response({'error': "id param is missing"})

#         user_check = UserProfiles.objects.filter(ls_aai_id=ls_aai_id)
#         if not user_check.exists():
#             return Response({'error': f'User with the LS AAI Id {ls_aai_id} does not exist'})

#         user_profile = UserProfiles.objects.get(ls_aai_id=ls_aai_id)
#         user_data = Users.objects.get(id=user_profile.user.id)

#         serializer = UsersSerializer(user_data)

#         return Response(serializer.data)


class UserStudyAccessCheck(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, study_id):
        uploaded = False    # To check if the study has been uploaded, if yes and has_access is no from checking DTPs, we check DUPs
        has_access = False

        if not study_id:
            return Response(status=400, data="Study ID missing")
        
        # Checking if study_id is UUID or sd_sid and if study with this id exists
        try:
            if not Studies.objects.filter(id=study_id).exists():
                return Response(status=404, data="Couldn't find study from study ID")
        except ValidationError: # sd_oid
            if Studies.objects.filter(sd_sid=study_id).exists():
                study_id = Studies.objects.get(sd_sid=study_id).id  # Need to use ID instead of sd_oid for the rest of the function
            else:
                return Response(status=404, data="Couldn't find study from study sd_sid")
        
        user_id = self.request.user.id

        # Checking if the study has been uploaded (=associated study of DTP + DTP at transfer status)
        # and in that case, if user is in associated people of the DTP
        dtp_studies = DtpStudies.objects.filter(study=study_id)
        for dtp_study in dtp_studies:   # Should be only one
            # May be false if somehow a deletion of a DTP didn't delete records in DTP Study table
            if DataTransferProcesses.objects.filter(id=dtp_study.dtp_id.id).exists():
                dtp = DataTransferProcesses.objects.get(id=dtp_study.dtp_id.id)
                # TODO: transfer status does not necessarily mean that the data has been uploaded, need to change DTP
                if dtp.status and hasattr(dtp.status, "list_order") and dtp.status.list_order == DTP_STATUS_INDEX_TRANSFER:
                    uploaded = True
                    dtp_people_check = DtpPeople.objects.filter(dtp_id=dtp.id, person=user_id)
                    if dtp_people_check.exists():
                        has_access = True
                        break

        if uploaded and not has_access:  # Check DUPs
            # Getting all DUP users entries for this user
            dup_users = DupPeople.objects.filter(person=user_id)

            for dup_user in dup_users:
                # May be false if somehow a deletion of a DUP didn't delete records in DUP People table
                if DataUseProcesses.objects.filter(id=dup_user.dup_id.id).exists():
                    dup = DataUseProcesses.objects.get(id=dup_user.dup_id.id)
                    # Access only if DUP is at "access granted status"
                    if dup.status and hasattr(dup.status, "list_order") and dup.status.list_order == DUP_STATUS_INDEX_ACCESS_GRANTED:
                        dup_studies = DupStudies.objects.filter(dup_id=dup_user.dup_id)
                        for dup_study in dup_studies:
                            if dup_study.study.id == study_id:
                                has_access = True
                                break

        return Response(data={"has_access": has_access})


class UserDOAccessCheck(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, do_id):
        uploaded = False    # To check if the DO has been uploaded, if yes and has_access is no from checking DTPs, we check DUPs
        has_access = False

        if not do_id:
            return Response(status=400, data="Object ID missing")
        
        # Checking if do_id is UUID or sd_oid and if DO with this id exists
        try:
            if not DataObjects.objects.filter(id=do_id).exists():
                return Response(status=404, data="Couldn't find DO from DO ID")
        except ValidationError: # sd_oid
            if DataObjects.objects.filter(sd_oid=do_id).exists():
                do_id = DataObjects.objects.get(sd_oid=do_id).id    # Need to use ID instead of sd_oid for the rest of the function
            else:
                return Response(status=404, data="Couldn't find DO from DO sdOid")

        user_id = self.request.user.id

        # Checking if the DO has been uploaded (=associated DO of DTP + DTP at transfer status)
        # and in that case, if user is in associated people of the DTP
        dtp_dos = DtpObjects.objects.filter(data_object=do_id)
        for dtp_do in dtp_dos:   # Should be only one
            # May be false if somehow a deletion of a DTP didn't delete records in DTP Study table
            if DataTransferProcesses.objects.filter(id=dtp_do.dtp_id.id).exists():
                dtp = DataTransferProcesses.objects.get(id=dtp_do.dtp_id.id)
                # TODO: same as above TODO
                if dtp.status and hasattr(dtp.status, "list_order") and dtp.status.list_order == DTP_STATUS_INDEX_TRANSFER:
                    uploaded = True
                    dtp_people_check = DtpPeople.objects.filter(dtp_id=dtp.id, person=user_id)
                    if dtp_people_check.exists():
                        has_access = True
                        break

        if uploaded and not has_access:  # Check DUPs
            # Getting all DUP users entries for this user
            dup_users = DupPeople.objects.filter(person=user_id)

            for dup_user in dup_users:
                # May be false if somehow a deletion of a DUP didn't delete records in DUP People table
                if DataUseProcesses.objects.filter(id=dup_user.dup_id.id).exists():
                    dup = DataUseProcesses.objects.get(id=dup_user.dup_id.id)
                    # Access only if DUP is at "access granted status"
                    if dup.status and hasattr(dup.status, "list_order") and dup.status.list_order == DUP_STATUS_INDEX_ACCESS_GRANTED:
                        dup_objects = DupObjects.objects.filter(dup_id=dup_user.dup_id)
                        for dup_do in dup_objects:
                            if dup_do.data_object.id == do_id:
                                has_access = True
                                break

        return Response(data={"has_access": has_access})


class UserDUPAccessData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = self.request.user

        user_profile = UserProfiles.objects.filter(user=user.id)
        if not user_profile.exists():
            return Response(status=404, data="User profile not found")
        
        # Getting all DUP users entries for this user
        dup_users = DupPeople.objects.filter(person=user.id)

        do_id_list = []

        for dup_user in dup_users:
            # May be false if somehow a deletion of a DUP didn't delete records in DUP People table
            if DataUseProcesses.objects.filter(id=dup_user.dup_id.id).exists():
                dup = DataUseProcesses.objects.get(id=dup_user.dup_id.id)
                # Access only if DUP is at "access granted status"
                if dup.status and hasattr(dup.status, "list_order") and dup.status.list_order == DUP_STATUS_INDEX_ACCESS_GRANTED:
                    dup_objects = DupObjects.objects.filter(dup_id=dup_user.dup_id)
                    for dup_do in dup_objects:
                        do_id_list.append(dup_do.data_object.id)
        
        do_id_set = set(do_id_list)
        data_objects = DataObjects.objects.filter(id__in=do_id_set)

        studies_dict = {}
        for do in data_objects:
            if do.linked_study.sd_sid in studies_dict:
                studies_dict[do.linked_study.sd_sid].dos_access_granted.append(do)
            else:
                studies_dict[do.linked_study.sd_sid] = do.linked_study
                # studies_dict[do.linked_study.sd_sid]["dos_access_granted"] = [do]
                setattr(studies_dict[do.linked_study.sd_sid], "dos_access_granted", [do])
        studies = studies_dict.values()

        serializer = StudyDUPSerializer(studies, many=True)
        return Response(serializer.data)


class UserAccessData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, userId):
        user = Users.objects.filter(id=userId)
        if not user.exists():
            return Response(status=404, data="User not found")

        user_profile = UserProfiles.objects.filter(user=userId)
        if not user_profile.exists():
            return Response(status=404, data="User profile not found")

        """ Write perms (DTP) """
        # List of DTP IDs for one user
        dtp_users = DtpPeople.objects.filter(person=userId)

        write_do_id_list = []

        for dtp_user in dtp_users:
            dtp_dos = DtpObjects.objects.filter(dtp_id=dtp_user.dtp_id)
            
            for dtp_do in dtp_dos:
                dtp_check = DataTransferProcesses.objects.filter(id=dtp_do.dtp_id).exists
                if dtp_check.exists():
                    dtp = DataTransferProcesses.objects.get(id=dtp_do.dtp_id)
                    if dtp.status and has_attr(dtp.status, list_order) and dtp.status.name.list_order == DTP_STATUS_INDEX_TRANSFER:
                        write_do_id_list.append(dtp_do.data_object.id)

        write_do_id_set = set(write_do_id_list)

        """ Access perms (DUP) """
        # List of DUP IDs for one user
        dup_users = DupPeople.objects.filter(person=userId)

        read_do_id_list = []

        for dup_user in dup_users:
            # May be false if somehow a deletion of a DUP didn't delete records in DUP People table
            if DataUseProcesses.objects.filter(id=dup_user.dup_id.id).exists():
                dup = DataUseProcesses.objects.get(id=dup_user.dup_id.id)
                if dup.agreement_signed_date: # Read perm only if DUP is at "availability of the data" step
                    dup_objects = DupObjects.objects.filter(dup_id=dup_user.dup_id)
                    for dup_do in dup_objects:
                        read_do_id_list.append(dup_do.data_object.id)
        
        read_do_id_set = set(read_do_id_list)

        """ Public DOs """
        public_access_type = ObjectAccessTypes.objects.get(name="Public")
        public_dos_set = set(DataObjects.objects.filter(access_type=public_access_type.id).values_list('id', flat=True))

        all_do_ids_set = read_do_id_set.union(write_do_id_set).union(public_dos_set)
        data_objects = DataObjects.objects.filter(id__in=all_do_ids_set)
        linked_studies = set(data_objects.values_list('linked_study', flat=True))
        studies = Studies.objects.filter(id__in=linked_studies)

        response = {
            "studies": []
        }

        if studies.exists():
            for study in studies:
                data_objects = DataObjects.objects.filter(linked_study=study)
                data_objects_response = []
                if data_objects.exists():
                    for data_object in data_objects:
                        if data_object.id in all_do_ids_set:
                            # Embargo check
                            # TODO: still include embargoed DOs for submittors?
                            if not bool(data_object.embargo_expiry) or data_object.embargo_expiry.replace(tzinfo=None) <= datetime.datetime.now():
                                object_instances = ObjectInstances.objects.filter(data_object=data_object)
                                object_instances_response = []
                                if object_instances.exists():
                                    for object_instance in object_instances:
                                        object_instances_response.append({
                                            "id": object_instance.id,
                                            "sdIid": object_instance.sd_iid,
                                            "sdOid": data_object.sd_oid,
                                            "url": object_instance.url,
                                            "urlAccessible": object_instance.url_accessible,
                                            "repository": object_instance.repository,
                                        })
                                data_objects_response.append({
                                    "objectId": data_object.id,
                                    "sdOid": data_object.sd_oid,
                                    "objectTitle": data_object.display_title,
                                    "objectDescription": "",
                                    "objectInstances": object_instances_response,
                                    "accessType": data_object.access_type.name if data_object.access_type else "",
                                    "embargoExpiry": data_object.embargo_expiry,
                                    "userPerms": "rw" if data_object.id in write_do_id_set else "r"
                                })

                if len(data_objects_response) > 0:
                    response["studies"].append({
                        "studyId": study.id,
                        "sdSid": study.sd_sid,
                        "studyTitle": study.display_title,
                        "dataObjects": data_objects_response
                    })

        return Response(response, status=200)


class UsersToNotify(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [IsSuperUser]

    def get(self, request, sd_oid):
        do_check = DataObjects.objects.filter(sd_oid=sd_oid)

        if not do_check.exists():
             return Response(status=404, data="Data Object not found")
        else:
            do = DataObjects.objects.get(sd_oid=sd_oid)
            # Get DTPs where DO is linked as associated object (should be only 1 in practice)
            dtp_ids = list(DtpObjects.objects.filter(data_object=do).values_list('dtp_id', flat=True))
            # Get DTP associated people
            dtp_users = list(DtpPeople.objects.filter(dtp_id__in=dtp_ids).values_list('person_id', flat=True))
            # Get users only and not people
            users_to_notify = list(UserProfiles.objects.filter(user_id__in=dtp_users).filter(~Q(ls_aai_id='')).values_list('user_id', flat=True))

            return Response({"user_ids": users_to_notify}, status=200)
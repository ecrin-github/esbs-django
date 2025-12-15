import json

from mozilla_django_oidc.contrib.drf import OIDCAuthentication
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from app.permissions import ReadOnly, IsSuperUser
from app.serializers import MailSerializer
from configs.app_settings import EMAIL_MAIN_RECIPIENT
from context.models.dup_status_types import DupStatusTypes
from context.serializers.dup_status_types_dto import DupStatusTypesOutputSerializer
from general.models.organisations import Organisations
from general.serializers.organisations_dto import OrganisationsInputSerializer
from mdm.views.common.mixins import GetAuthFilteringMixin
from rms.models.dup.data_access_request import DataAccessRequest
from rms.models.dup.duas import DataUseAgreements
from rms.models.dup.dup_notes import DupNotes
from rms.models.dup.dup_objects import DupObjects
from rms.models.dup.dup_people import DupPeople
from rms.models.dup.dup_prereqs import DupPrereqs
from rms.models.dup.dup_secondary_use import DupSecondaryUse
from rms.models.dup.dup_studies import DupStudies
from rms.models.dup.dups import DataUseProcesses
from rms.serializers.dup.data_access_request_dto import *
from rms.serializers.dup.duas_dto import DataUseAgreementsOutputSerializer, DataUseAgreementsInputSerializer
from rms.serializers.dup.dup_notes_dto import DupNotesOutputSerializer, DupNotesInputSerializer
from rms.serializers.dup.dup_objects_dto import DupObjectsOutputSerializer, DupObjectsInputSerializer
from rms.serializers.dup.dup_people_dto import DupPeopleOutputSerializer, DupPeopleInputSerializer
from rms.serializers.dup.dup_secondary_use_dto import DupSecondaryUseOutputSerializer, DupSecondaryUseInputSerializer
from rms.serializers.dup.dup_studies_dto import DupStudiesOutputSerializer, DupStudiesInputSerializer
from rms.serializers.dup.dups_dto import DataUseProcessesOutputSerializer, DataUseProcessesInputSerializer
from users.models.users import Users
from users.serializers.users_dto import CreateUserSerializer

import logging
LOGGER = logging.getLogger('django')


class DataUseAgreementsList(GetAuthFilteringMixin, viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DataUseAgreements.objects.all()
    object_class = DataUseAgreements
    serializer_class = DataUseAgreementsOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DataUseAgreementsInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        # TODO (for multiple views): return unauthorised error if trying to get DUAs for a unauthorised DUP instead of empty result set
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupNotesList(GetAuthFilteringMixin, viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DupNotes.objects.all()
    object_class = DupNotes
    serializer_class = DupNotesOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DupNotesInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupObjectsList(GetAuthFilteringMixin, viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DupObjects.objects.all()
    object_class = DupObjects
    serializer_class = DupObjectsOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DupObjectsInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupPeopleList(GetAuthFilteringMixin, viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DupPeople.objects.all()
    object_class = DupPeople
    serializer_class = DupPeopleOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DupPeopleInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupSecondaryUseList(GetAuthFilteringMixin, viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DupSecondaryUse.objects.all()
    obejct_class = DupSecondaryUse
    serializer_class = DupSecondaryUseOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DupSecondaryUseInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DupStudiesList(GetAuthFilteringMixin, viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DupStudies.objects.all()
    object_class = DupStudies
    serializer_class = DupStudiesOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DupStudiesInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(dup_id=self.kwargs['dupId'])
        )


class DataUseProcessesList(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DataUseProcesses.objects.all()
    object_class = DataUseProcesses
    serializer_class = DataUseProcessesOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DataUseProcessesInputSerializer
        return super().get_serializer_class()

    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return self.object_class.objects.none()
        user = self.request.user
        if user.is_superuser:
            return (
                super()
                .get_queryset(*args, **kwargs)
            )
        elif user.user_profile and user.user_profile.organisation:
            dup_id_set = set(map(lambda p: p.dup_id.id, DupPeople.objects.filter(person=user)))
            
            return (
                super()
                .get_queryset(*args, **kwargs)
                .filter(id__in=dup_id_set)
            )
        return self.object_class.objects.none()
    

class DataAccessRequestView(GetAuthFilteringMixin, viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DataAccessRequest.objects.all()
    object_class = DataAccessRequest
    serializer_class = DataAccessRequestOutputSerializer
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return DataAccessRequestInputSerializer
        return super().get_serializer_class()
    
    def get_user_id(self, name, email):
        user = None
        user_check = Users.objects.filter(email=email)

        if user_check.exists():
            user = Users.objects.get(email=email)
        else:
            user_serializer = CreateUserSerializer(data={'name': name, 'email': email})
            user_serializer.is_valid()
            user_serializer.save()
            user = Users.objects.get(email=email)

        if user is not None:
            return user.id

        return user

    def create(self, request, *args, **kwargs):
        # Handling organisation
        if 'organisation' in request.data:
            if 'id' in request.data['organisation'] and not request.data['organisation']['id']:
                org = OrganisationsInputSerializer(data=request.data['organisation'])
                org.is_valid()
                org.save()

                org_check = Organisations.objects.filter(default_name=request.data['organisation']['default_name'], 
                                                            city=request.data['organisation']['city'],
                                                            country_name=request.data['organisation']['country_name'])
                if org_check.exists():
                    org = Organisations.objects.get(default_name=request.data['organisation']['default_name'], 
                                                            city=request.data['organisation']['city'],
                                                            country_name=request.data['organisation']['country_name'])
                    request.data['organisation'] = org.id
        
        # Handling principal secondary user
        if 'principal_secondary_user' in request.data:
            principal_user = request.data['principal_secondary_user']
            name = principal_user['name']
            email = principal_user['email'].lower()
            user_id = self.get_user_id(name, email)
            if user_id is not None:
                request.data['principal_secondary_user'] = user_id
            else:
                request.data['principal_secondary_user'] = None
        
        # Handling additional secondary users
        additional_user_ids = []
        if 'additional_secondary_users' in request.data:
            for additional_user in request.data['additional_secondary_users']:
                if 'name' in additional_user and 'email' in additional_user:
                    name = additional_user['name']
                    email = additional_user['email'].lower()
                    user_id = self.get_user_id(name, email)
                    if user_id is not None:
                        additional_user_ids.append(user_id)
        request.data['additional_secondary_users'] = additional_user_ids

        # Saving access request
        input_serializer = self.get_serializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        self.perform_create(input_serializer)

        output_serializer = DataAccessRequestOutputSerializer(input_serializer.instance)
        
        return Response(output_serializer.data)

    def perform_create(self, serializer):
        serializer.save()


class DataAccessRequestSubmission(APIView):
    parser_classes = [MultiPartParser, FormParser]
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DataAccessRequest.objects.all()
    object_class = DataAccessRequest
    serializer_class = DataAccessRequestOutputSerializer
    permission_classes = [permissions.AllowAny]

    def get_email_content(self, dar, requester_name, requester_email):
        content = ('<b>Requestor Name: </b>' + requester_name + '<br />' +
            '<b>Requestor Email: </b>' + requester_email + '<br />' +
            '<b><h4>Data requesting organisation</h4></b>')
        content += ('<b>Name: </b>' + dar["organisation"]["default_name"] + '<br />' +
            '<b>Address: </b>' + dar["organisation_address"]+ '<br />' +
            '<b><h4>Principal Data Secondary User</h4></b>' +
            '<b>Name: </b>' + dar["principal_secondary_user"]["first_name"] + ' ' + dar["principal_secondary_user"]["last_name"] + '<br />' +
            '<b>Email: </b>' + dar["principal_secondary_user"]["email"] + '<br />' +
            '<b>CV attached</b>' +
            '<b><h4>Additional secondary users</h4></b>')

        if (len(dar["additional_secondary_users"])> 0):
            for u in dar["additional_secondary_users"]:
                content += ('<b>Name: </b>' + u["first_name"] + ' ' + u["last_name"] + '<br />' +
                        '<b>Email: </b>' + u["email"] + '<br/>-<br/>')
        else:
            content += '/<br/>-<br/>'

        content += ('<b><h4>Requested study for secondary use</h4></b>' +
                    (dar["requested_study"]["sd_sid"] if dar["requested_study"]["sd_sid"] else 'Missing study ID') + ' - ' + 
                    (dar["requested_study"]["display_title"] if dar["requested_study"]["display_title"] else 'Missing study title') +
                    '<b><h4>Controlled access data objects</h4></b>')
        if (len(dar["requested_study"]["linked_objects"]) > 0):
            for o in dar["requested_study"]["linked_objects"]:
                if "access_type" in o and "name" in o["access_type"] and o["access_type"]["name"].lower() == "controlled":
                    content += o["sd_oid"] + ' - ' + o["display_title"] + '<br />'
        else:
            content += '/'
        content += ('<b><h4>Secondary Use Project</h4></b>' +
                    '<b>Title: </b>' + dar["project_title"]+ '<br />' +
                    '<b>Type: </b>' + dar["project_type"]+ '<br />' +
                    '<b>Abstract/Description: </b>' + dar["project_abstract"]+ '<br />' +
                    '<b>Ethics Approval: </b>' + dar["ethics_approval"]+ '<br />' +
                    '<b>Ethics Approval Details: </b>' + dar["ethics_approval_details"]+ '<br />' +
                    '<b>Funding: </b>' + (dar["project_funding"] if dar["project_funding"] else '/') + '<br />' +
                    '<b>Estimated Access Duration Required: </b>' + (dar["estimated_access_duration_required"] if dar["estimated_access_duration_required"] else '/') + '<br />' +
                    '<b>Provisional Starting Date: </b>' + (dar["provisional_starting_date"] if dar["provisional_starting_date"] else '/') + '<br />' +
                    '<b><h4>Other info</h4></b>' + 
                    (dar["other_info"] if dar["other_info"] else '/'))
        return content
    
    def get_user_id(self, name, email):
        user = None
        user_check = Users.objects.filter(email=email)

        if user_check.exists():
            user = Users.objects.get(email=email)
        else:
            user_serializer = CreateUserSerializer(data={'name': name, 'email': email})
            user_serializer.is_valid()
            user_serializer.save()
            user = Users.objects.get(email=email)

        if user is not None:
            return user.id

        return user

    def get(self, request):
        serializer = DataAccessRequestOutputSerializer(DataAccessRequest.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        form_data = request.data.copy()

        # Handling organisation
        if 'organisation' in form_data:
            form_data['organisation'] = json.loads(form_data['organisation'])
            if 'id' not in form_data['organisation']:
                org = OrganisationsInputSerializer(data={'default_name': form_data['organisation']['default_name'],
                                                        'city': form_data['organisation']['city'],
                                                        'country_name': form_data['organisation']['country_name']})
                org.is_valid()
                org.save()

            org_check = Organisations.objects.filter(default_name=form_data['organisation']['default_name'], 
                                                        city=form_data['organisation']['city'],
                                                        country_name=form_data['organisation']['country_name'])
            if org_check.exists():
                org = Organisations.objects.get(default_name=form_data['organisation']['default_name'], 
                                                        city=form_data['organisation']['city'],
                                                        country_name=form_data['organisation']['country_name'])
                form_data['organisation'] = org.id
        
        cc_emails = []

        # Handling principal secondary user
        if 'principal_secondary_user' in form_data:
            principal_user = json.loads(form_data['principal_secondary_user'])
            name = principal_user['name']
            email = principal_user['email'].lower()
            user_id = self.get_user_id(name, email)
            if user_id is not None:
                form_data['principal_secondary_user'] = user_id
                cc_emails.append(email)
            else:
                form_data['principal_secondary_user'] = None
        
        # Handling additional secondary users
        additional_user_ids = []

        if 'additional_secondary_users' in form_data and form_data['additional_secondary_users']:
            for additional_user_str in form_data.getlist('additional_secondary_users', []):
                additional_user = json.loads(additional_user_str)
                if 'name' in additional_user and 'email' in additional_user:
                    name = additional_user['name']
                    email = additional_user['email'].lower()
                    user_id = self.get_user_id(name, email)
                    if user_id is not None:
                        additional_user_ids.append(str(user_id))
                        cc_emails.append(email)
        if len(additional_user_ids) > 0:
            form_data.setlist('additional_secondary_users', additional_user_ids)
        else:
            form_data.pop('additional_secondary_users', None)

        # Saving access request
        input_serializer = DataAccessRequestInputSerializer(data=form_data)
        input_serializer.is_valid(raise_exception=True)
        self.perform_create(input_serializer)

        output_serializer = DataAccessRequestOutputSerializer(input_serializer.instance)

        # Creating a DUP instance
        dup_status = None
        if DupStatusTypes.objects.filter(list_order=0).exists():   # Request under review status
            dup_status = DupStatusTypes.objects.get(list_order=0).id
        
        dup_data = {
            "display_name": f"Data Access Request ({output_serializer.data['organisation']['default_name']})",
            "organisation": output_serializer.data["organisation"]["id"], 
            "status": dup_status, # Need a new status?
            "data_access_request": output_serializer.data["id"]
        }
        dup_serializer = DataUseProcessesInputSerializer(data=dup_data)
        dup_serializer.is_valid(raise_exception=True)
        dup_instance = dup_serializer.save()

        # Associating people (creating DUP People)
        if "id" in output_serializer.data["principal_secondary_user"]:
            dup_people_serializer = DupPeopleInputSerializer(data={"dup_id": dup_instance.id, "person": output_serializer.data["principal_secondary_user"]["id"]})
            dup_people_serializer.is_valid(raise_exception=True)
            dup_people_serializer.save()
        for additional_user_id in additional_user_ids:
            dup_people_serializer = DupPeopleInputSerializer(data={"dup_id": dup_instance.id, "person": additional_user_id})
            dup_people_serializer.is_valid(raise_exception=True)
            dup_people_serializer.save()
        
        # Associating study (creating DUP Study)
        dup_study_serializer = DupStudiesInputSerializer(data={"dup_id": dup_instance.id, "study": output_serializer.data["requested_study"]["id"]})
        dup_study_serializer.is_valid(raise_exception=True)
        dup_study_instance = dup_study_serializer.save()

        # Associating DOs (creating DUP Objects), to be changed in the future with selection of specific DOs in study
        if "linked_objects" in output_serializer.data["requested_study"]:
            for data_object in output_serializer.data["requested_study"]["linked_objects"]:
                if "access_type" in data_object and "name" in data_object["access_type"] and data_object["access_type"]["name"].lower() == "controlled":
                    dup_object_serializer = DupObjectsInputSerializer(data={"dup_id": dup_instance.id, "data_object": data_object["id"], "study": dup_study_instance.id})
                    dup_object_serializer.is_valid(raise_exception=True)
                    dup_object_serializer.save()

        if form_data["requester_email"] not in cc_emails:
            cc_emails.append(form_data["requester_email"])

        # Sending email
        mail_data = {
            "subject": "crDSR Data Access Request",
            "message": self.get_email_content(output_serializer.data, form_data["requester_name"], form_data["requester_email"]),
            "cv": output_serializer.data["cv"],
            "cc": ','.join(cc_emails)
        }

        serializer = MailSerializer(data=mail_data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success'}, status=200)

        return Response(serializer.errors, status=400)
        
    def perform_create(self, serializer):
        serializer.save()
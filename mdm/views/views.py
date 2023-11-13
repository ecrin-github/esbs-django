import json

import psycopg2
import requests
from mozilla_django_oidc.contrib.drf import OIDCAuthentication
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from configs.remote_db_settings import (REMOTE_DB_USER, REMOTE_DB_PASSWORD, REMOTE_DB_HOST, REMOTE_DB_PORT,
                                        REMOTE_RMS_DB_NAME)
from context.models import TrialRegistries
from db_exports.export_context_and_general_data import get_data_from_table
from general.models import Organisations
from mdm.models import DataObjects, StudyContributors, Studies
from mdm.serializers.data_object.data_objects_dto import DataObjectsOutputSerializer
from rms.models import DataTransferProcesses, DataUseProcesses, DtpObjects, DupObjects, DupStudies, DtpStudies


rms_db_connection = psycopg2.connect(
    user=REMOTE_DB_USER,
    password=REMOTE_DB_PASSWORD,
    host=REMOTE_DB_HOST,
    port=REMOTE_DB_PORT,
    database=REMOTE_RMS_DB_NAME
)


class MdrStudiesData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        reg_id = self.request.query_params.get('regId')
        sd_sid = self.request.query_params.get('sdSid')

        if reg_id is None:
            return Response({'error': "regId param is missing"})
        if sd_sid is None:
            return Response({'error': "sdSid param is missing"})

        trial_registry_check = TrialRegistries.objects.filter(id=reg_id)
        if not trial_registry_check.exists():
            return Response({'error': "Trial registry does not exist"})

        trial_registry = TrialRegistries.objects.get(id=reg_id)
        records = get_data_from_table('rms', 'lup', 'trial_registries')

        trial_registry_id = None

        for record in records:
            if record[1] == trial_registry.name:
                trial_registry_id = record[0]
                break

        if trial_registry_id is None:
            return Response({'error': "Trial registry does not exist in the MDR database"})

        res = requests.get(
            f"https://api.ecrin-rms.org/api/studies/mdr/{trial_registry_id}/{sd_sid}/data",
            headers={'Authorization': request.META['HTTP_AUTHORIZATION']}
        )
        json_res = json.loads(res.text)

        return Response(json_res)


class MdrStudies(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        reg_id = self.request.query_params.get('regId')
        sd_sid = self.request.query_params.get('sdSid')

        if reg_id is None:
            return Response({'error': "regId param is missing"})
        if sd_sid is None:
            return Response({'error': "sdSid param is missing"})

        trial_registry_check = TrialRegistries.objects.filter(id=reg_id)
        if not trial_registry_check.exists():
            return Response({'error': "Trial registry does not exist"})

        trial_registry = TrialRegistries.objects.get(id=reg_id)
        records = get_data_from_table('rms', 'lup', 'trial_registries')

        trial_registry_id = None

        for record in records:
            if record[1] == trial_registry.name:
                trial_registry_id = record[0]
                break

        if trial_registry_id is None:
            return Response({'error': "Trial registry does not exist in the MDR database"})

        res = requests.get(
            f"https://api.ecrin-rms.org/api/studies/mdr/{trial_registry_id}/{sd_sid}",
            headers={'Authorization': request.META['HTTP_AUTHORIZATION']}
        )
        json_res = json.loads(res.text)

        return Response(json_res)


class MdrDataObjects(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        mdr_id = self.request.query_params.get('mdrId')
        sd_sid = self.request.query_params.get('sdSid')

        if mdr_id is None:
            return Response({'error': "mdrId param is missing"})
        if sd_sid is None:
            return Response({'error': "sdSid param is missing"})

        res = requests.get(
            f"https://api.ecrin-rms.org/api/data-objects/mdr/{sd_sid}/{mdr_id}",
            headers={'Authorization': request.META['HTTP_AUTHORIZATION']}
        )
        json_res = json.loads(res.text)

        return Response(json_res)


class DtpByOrg(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        org_id = self.request.query_params.get('orgId')

        if org_id is None:
            return Response({'error': "orgId param is missing"})

        org_check = Organisations.objects.filter(id=org_id)
        if not org_check.exists():
            return Response({'error': f"Organisation with the orgId {org_id} does not exist."})

        data = DataTransferProcesses.objects.filter(organisation=org_check)

        return Response(data)


class DupByOrg(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        org_id = self.request.query_params.get('orgId')

        if org_id is None:
            return Response({'error': "orgId param is missing"})

        org_check = Organisations.objects.filter(id=org_id)
        if not org_check.exists():
            return Response({'error': f"Organisation with the orgId {org_id} does not exist."})

        data = DataUseProcesses.objects.filter(org_id=org_check)

        return Response(data)


class DataObjectsByOrg(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        org_id = self.request.query_params.get('orgId')

        if org_id is None:
            return Response({'error': "orgId param is missing"})

        org_check = Organisations.objects.filter(id=org_id)
        if not org_check.exists():
            return Response({'error': f"Organisation with the orgId {org_id} does not exist."})

        data = DataObjects.objects.filter(managing_org=org_check)

        return Response(data)


class StudiesByOrg(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        org_id = self.request.query_params.get('orgId')

        if org_id is None:
            return Response({'error': "orgId param is missing"})

        org_check = Organisations.objects.filter(id=org_id)
        if not org_check.exists():
            return Response({'error': f"Organisation with the orgId {org_id} does not exist."})

        data = StudyContributors.objects.filter(organisation=org_check)
        study_ids = []
        for rec in data:
            study_ids.append(rec.study_id)

        studies = Studies.objects.filter(id__in=study_ids)

        return Response(studies)


class DtpObjectInvolvement(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        object_id = self.request.query_params.get('objectId')

        if object_id is None:
            return Response({'error': "objectId param is missing"})

        object_check = DataObjects.objects.filter(id=object_id)
        if not object_check.exists():
            return Response({'error': f"Data object with the ID {object_id} does not exist."})

        d_object = DataObjects.objects.get(id=object_id)
        data = DtpObjects.objects.filter(object_id=d_object)
        return Response({'isInvolved': data.exists(), 'count': data.count()})


class DupObjectInvolvement(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        object_id = self.request.query_params.get('objectId')

        if object_id is None:
            return Response({'error': "objectId param is missing"})

        object_check = DataObjects.objects.filter(id=object_id)
        if not object_check.exists():
            return Response({'error': f"Data object with the ID {object_id} does not exist."})

        d_object = DataObjects.objects.get(id=object_id)
        data = DupObjects.objects.filter(object_id=d_object)
        return Response({'isInvolved': data.exists(), 'count': data.count()})


class DupStudyInvolvement(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        study_id = self.request.query_params.get('studyId')

        if study_id is None:
            return Response({'error': "studyId param is missing"})

        study_check = Studies.objects.filter(id=study_id)
        if not study_check.exists():
            return Response({'error': f"Study with the ID {study_id} does not exist."})

        study = Studies.objects.get(id=study_id)
        data = DupStudies.objects.filter(study_id=study)
        return Response({'isInvolved': data.exists(), 'count': data.count()})


class DtpStudyInvolvement(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        study_id = self.request.query_params.get('studyId')

        if study_id is None:
            return Response({'error': "studyId param is missing"})

        study_check = Studies.objects.filter(id=study_id)
        if not study_check.exists():
            return Response({'error': f"Study with the ID {study_id} does not exist."})

        study = Studies.objects.get(id=study_id)
        data = DtpStudies.objects.filter(study_id=study)
        return Response(
            {
                'isInvolved': data.exists(),
                'count': data.count()
            })


class MultiStudiesObjects(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        studies_ids = self.request.query_params.get('studiesIds').split(',')

        if studies_ids is None:
            return Response({'error': "studiesIds param is missing"})

        data = []

        for studyId in studies_ids:
            studies_check = Studies.objects.filter(id=studyId)
            if not studies_check.exists():
                return Response({'error': f"Study with the ID {studyId} does not exist."})

            study = Studies.objects.get(id=studyId)
            data_objects = DataObjects.objects.filter(linked_study=study)
            if data_objects.exists():
                serialized_data = DataObjectsOutputSerializer(data_objects, many=True)
                for rec in serialized_data.data:
                    data.append(rec)

        return Response({'data': data})


class DtpStudiesObjectsInvolvements(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, dtpId, format=None):
        if dtpId is None:
            return Response({'error': "dtpId param is missing"})

        dtp_check = DataTransferProcesses.objects.filter(id=dtpId)
        if not dtp_check.exists():
            return Response({'error': f"Data transfer process with the ID {dtpId} does not exist."})

        dtp = DataTransferProcesses.objects.get(id=dtpId)

        study_id = self.request.query_params.get('studyId')

        if study_id is None:
            return Response({'error': "studyId param is missing"})

        study_check = Studies.objects.filter(id=study_id)
        if not study_check.exists():
            return Response({'error': f"Study with the ID {study_id} does not exist."})
        study = Studies.objects.get(id=study_id)

        dtp_studies_check = DtpStudies.objects.filter(study_id=study, dtp_id=dtp)

        data = {
            "DtpTotal": dtp_studies_check.count(),
        }

        study_objects_check = DataObjects.objects.filter(linked_study=study)
        if not study_objects_check.exists():
            return Response(data)

        for rec in study_objects_check:
            data_obj = DataObjects.objects.get(id=rec.id)
            dtp_objects_check = DtpObjects.objects.filter(object_id=data_obj, dtp_id=dtp)
            if not dtp_objects_check.exists():
                continue
            data['DtpTotal'] += dtp_objects_check.count()

        return Response(data)


class DupStudiesObjectsInvolvements(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, dupId, format=None):
        if dupId is None:
            return Response({'error': "dupId param is missing"})

        dup_check = DataUseProcesses.objects.filter(id=dupId)
        if not dup_check.exists():
            return Response({'error': f"Data use process with the ID {dupId} does not exist."})

        dup = DataUseProcesses.objects.get(id=dupId)

        study_id = self.request.query_params.get('studyId')

        if study_id is None:
            return Response({'error': "studyId param is missing"})

        study_check = Studies.objects.filter(id=study_id)
        if not study_check.exists():
            return Response({'error': f"Study with the ID {study_id} does not exist."})
        study = Studies.objects.get(id=study_id)

        dup_studies_check = DupStudies.objects.filter(study_id=study, dup_id=dup)

        data = {
            "DupTotal": dup_studies_check.count(),
        }

        study_objects_check = DataObjects.objects.filter(linked_study=study)
        if not study_objects_check.exists():
            return Response(data)

        for rec in study_objects_check:
            data_obj = DataObjects.objects.get(id=rec.id)
            dup_objects_check = DupObjects.objects.filter(object_id=data_obj, dup_id=dup)
            if not dup_objects_check.exists():
                continue
            data['DupTotal'] += dup_objects_check.count()

        return Response(data)


class DtpDupStudiesObjectsInvolvements(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, dtpId, dupId, format=None):
        if dtpId is None:
            return Response({'error': "dtpId param is missing"})

        dtp_check = DataTransferProcesses.objects.filter(id=dtpId)
        if not dtp_check.exists():
            return Response({'error': f"Data transfer process with the ID {dtpId} does not exist."})

        dtp = DataTransferProcesses.objects.get(id=dtpId)

        if dupId is None:
            return Response({'error': "dupId param is missing"})

        dup_check = DataUseProcesses.objects.filter(id=dupId)
        if not dup_check.exists():
            return Response({'error': f"Data use process with the ID {dupId} does not exist."})

        dup = DataUseProcesses.objects.get(id=dupId)

        study_id = self.request.query_params.get('studyId')

        if study_id is None:
            return Response({'error': "studyId param is missing"})

        study_check = Studies.objects.filter(id=study_id)
        if not study_check.exists():
            return Response({'error': f"Study with the ID {study_id} does not exist."})
        study = Studies.objects.get(id=study_id)

        dtp_studies_check = DtpStudies.objects.filter(study_id=study, dtp_id=dtp)
        dup_studies_check = DupStudies.objects.filter(study_id=study, dup_id=dup)

        data = {
            "DtpTotal": dtp_studies_check.count(),
            "DupTotal": dup_studies_check.count(),
        }

        study_objects_check = DataObjects.objects.filter(linked_study=study)
        if not study_objects_check.exists():
            return Response(data)

        for rec in study_objects_check:
            data_obj = DataObjects.objects.get(id=rec.id)
            dtp_objects_check = DtpObjects.objects.filter(object_id=data_obj, dtp_id=dtp)
            dup_objects_check = DupObjects.objects.filter(object_id=data_obj, dup_id=dup)
            if dup_objects_check.exists():
                data['DupTotal'] += dup_objects_check.count()

            if dtp_objects_check.exists():
                data['DtpTotal'] += dtp_objects_check.count()

        return Response(data)

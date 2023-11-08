import json

import requests
from mozilla_django_oidc.contrib.drf import OIDCAuthentication
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from general.models import Organisations
from mdm.models import DataObjects, StudyContributors, Studies
from mdm.serializers.data_object.data_objects_dto import DataObjectsOutputSerializer
from rms.models import DataTransferProcesses, DataUseProcesses, DtpObjects, DupObjects, DupStudies, DtpStudies


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

        res = requests.get(
            f"https://api.ecrin-rms.org/api/studies/mdr/{reg_id}/{sd_sid}/data",
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

        res = requests.get(
            f"https://api.ecrin-rms.org/api/studies/mdr/{reg_id}/{sd_sid}",
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
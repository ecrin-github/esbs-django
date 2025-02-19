import json

import psycopg2
import requests
from mozilla_django_oidc.contrib.drf import OIDCAuthentication
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from app.permissions import IsSuperUser, WriteOnlyForOwnOrg, ReadOnly
from context.models.access_prereq_types import AccessPrereqTypes
from context.models import TrialRegistries, StudyTypes, StudyStatuses, GenderEligibilityTypes, TimeUnits
from context.serializers.access_prereq_types_dto import AccessPrereqTypesOutputSerializer
from db_exports.export_context_and_general_data import get_data_from_table
from general.models import Organisations
from mdm.models import DataObjects, StudyContributors, Studies
from mdm.serializers.data_object.data_objects_dto import DataObjectsOutputSerializer, DataObjectsLimitedOutputSerializer
from mdm.serializers.study.studies_dto import StudiesLimitedOutputSerializer
from mdm.views.common.mixins import GetAuthFilteringMixin
from rms.models import DataTransferProcesses, DataUseProcesses, DtpObjects, DupObjects, DupStudies, DtpStudies
from rms.models.dtp.dtp_prereqs import DtpPrereqs
from rms.serializers.dtp.dtp_prereqs_dto import DtpPrereqsOutputSerializer
from rms.serializers.dtp.dtps_dto import DataTransferProcessesOutputSerializer
from rms.serializers.dup.dups_dto import DataUseProcessesOutputSerializer


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

        # TODO
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


class DtpByOrg(GetAuthFilteringMixin, GenericAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DataTransferProcesses.objects.all()
    object_class = DataTransferProcesses
    serializer_class = DataTransferProcessesOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

    def get(self, request, *args, **kwargs):
        org_id = self.request.query_params.get('orgId')

        if org_id is None:
            return Response({'error': "orgId param is missing"})

        org_check = Organisations.objects.filter(id=org_id)
        if not org_check.exists():
            return Response({'error': f"Organisation with the orgId {org_id} does not exist."})

        org_data = Organisations.objects.get(id=org_id)

        data = self.get_queryset(*args, **kwargs).filter(organisation=org_data)
        serializer = self.get_serializer_class()(data, many=True)

        return Response(serializer.data)


class DupByOrg(GetAuthFilteringMixin, GenericAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DataUseProcesses.objects.all()
    object_class = DataUseProcesses
    serializer_class = DataUseProcessesOutputSerializer
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

    def get(self, request, *args, **kwargs):
        org_id = self.request.query_params.get('orgId')

        if org_id is None:
            return Response({'error': "orgId param is missing"})

        org_check = Organisations.objects.filter(id=org_id)
        if not org_check.exists():
            return Response({'error': f"Organisation with the orgId {org_id} does not exist."})

        org_data = Organisations.objects.get(id=org_id)

        data = self.get_queryset(*args, **kwargs).filter(organisation=org_data)
        serializer = self.get_serializer_class()(data, many=True)

        return Response(serializer.data)


class DataObjectsByOrg(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        org_id = self.request.query_params.get('orgId')

        if org_id is None:
            return Response({'error': "orgId param is missing"})

        org_check = Organisations.objects.filter(id=org_id)
        if not org_check.exists():
            return Response({'error': f"Organisation with the orgId {org_id} does not exist."})

        data = DataObjects.objects.filter(organisation=org_id)
        serializer = DataObjectsLimitedOutputSerializer(data, many=True)

        return Response(serializer.data)


class StudiesByOrg(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        org_id = self.request.query_params.get('orgId')

        if org_id is None:
            return Response({'error': "orgId param is missing"})

        org_check = Organisations.objects.filter(id=org_id)
        if not org_check.exists():
            return Response({'error': f"Organisation with the orgId {org_id} does not exist."})

        studies = Studies.objects.filter(organisation=org_id)

        serializer = StudiesLimitedOutputSerializer(studies, many=True)

        return Response(serializer.data)


class DtpObjectInvolvement(APIView):
    # TODO: add GetAuthFilteringMixin here once dtp studies are added by dtp organisation
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

    def get(self, request):
        object_id = self.request.query_params.get('objectId')

        if object_id is None:
            return Response({'error': "objectId param is missing"})

        object_check = DataObjects.objects.filter(id=object_id)
        if not object_check.exists():
            return Response({'error': f"Data object with the ID {object_id} does not exist."})

        d_object = DataObjects.objects.get(id=object_id)
        data = DtpObjects.objects.filter(data_object=d_object)
        return Response({'isInvolved': data.exists(), 'count': data.count()})


class DupObjectInvolvement(APIView):
    # TODO: add GetAuthFilteringMixin here once dup studies are added by dup organisation
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

    def get(self, request):
        object_id = self.request.query_params.get('objectId')

        if object_id is None:
            return Response({'error': "objectId param is missing"})

        object_check = DataObjects.objects.filter(id=object_id)
        if not object_check.exists():
            return Response({'error': f"Data object with the ID {object_id} does not exist."})

        d_object = DataObjects.objects.get(id=object_id)
        data = DupObjects.objects.filter(data_object=d_object)
        return Response({'isInvolved': data.exists(), 'count': data.count()})


class DupStudyInvolvement(APIView):
    # TODO: add GetAuthFilteringMixin here once dup studies are added by dup organisation
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

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
    # TODO: add GetAuthFilteringMixin here once dtp studies are added by dtp organisation
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

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

class DupPrereqs(GetAuthFilteringMixin, GenericAPIView):
    # Fetches prereqs from DTP prereqs table
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    queryset = DtpPrereqs.objects.all()
    object_class = DtpPrereqs
    # TODO: use a smaller serializer (for objects)
    serializer_class = DtpPrereqsOutputSerializer
    permission_classes = [permissions.IsAuthenticated & ReadOnly]
    
    def get(self, request):
        do_ids = self.request.query_params.get('dataObjectIds').split(',')

        if do_ids is None:
            return Response({'error': "dataObjectIds param is missing"})

        data = []

        for do_id in do_ids:
            do_check = DataObjects.objects.filter(id=do_id)
            if not do_check.exists():
                return Response({'error': f"Data Object with the ID {do_id} does not exist."})

            dtp_dos = DtpObjects.objects.filter(data_object=do_id)
            if dtp_dos.exists():
                prereqs = DtpPrereqs.objects.filter(dtp_data_object__in=dtp_dos)
                if prereqs.exists():
                    serialized_data = self.get_serializer_class()(prereqs, many=True)
                    for rec in serialized_data.data:
                        data.append(rec)

        return Response({'data': data})


class MultiStudiesObjects(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        studies_ids = self.request.query_params.get('studiesIds').split(',')

        if studies_ids is None:
            return Response({'error': "studiesIds param is missing"})

        data = []

        for studyId in studies_ids:
            # Note: linkedStudies are still using internal id
            # TODO: filter on sdSid instead of studyId
            studies_check = Studies.objects.filter(id=studyId)
            if not studies_check.exists():
                return Response({'error': f"Study with the ID {studyId} does not exist."})

            study = Studies.objects.get(id=studyId)
            data_objects = DataObjects.objects.filter(linked_study=study)
            if data_objects.exists():
                serialized_data = DataObjectsLimitedOutputSerializer(data_objects, many=True)
                for rec in serialized_data.data:
                    data.append(rec)

        return Response({'data': data})


class DtpStudiesObjectsInvolvements(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [IsSuperUser]

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
            "studyAssociated": dtp_studies_check.exists(),
            "objectsAssociated": False,
        }

        study_objects_check = DataObjects.objects.filter(linked_study=study)
        if not study_objects_check.exists():
            return Response(data)

        for rec in study_objects_check:
            data_obj = DataObjects.objects.get(id=rec.id)
            dtp_objects_check = DtpObjects.objects.filter(data_object=data_obj, dtp_id=dtp)
            if not dtp_objects_check.exists():
                continue
            else:
                data['objectsAssociated'] = True
                break

        return Response(data)


class DupStudiesObjectsInvolvements(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [IsSuperUser]

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
            "studyAssociated": dup_studies_check.exists(),
            "objectsAssociated": False,
        }

        study_objects_check = DataObjects.objects.filter(linked_study=study)
        if not study_objects_check.exists():
            return Response(data)

        for rec in study_objects_check:
            data_obj = DataObjects.objects.get(id=rec.id)
            dup_objects_check = DupObjects.objects.filter(data_object=data_obj, dup_id=dup)
            if not dup_objects_check.exists():
                continue
            else:
                data['objectsAssociated'] = True
                break

        return Response(data)


# class DtpDupStudiesObjectsInvolvements(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
#     permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

#     def get(self, request, dtpId, dupId, format=None):
#         if dtpId is None:
#             return Response({'error': "dtpId param is missing"})

#         dtp_check = DataTransferProcesses.objects.filter(id=dtpId)
#         if not dtp_check.exists():
#             return Response({'error': f"Data transfer process with the ID {dtpId} does not exist."})

#         dtp = DataTransferProcesses.objects.get(id=dtpId)

#         if dupId is None:
#             return Response({'error': "dupId param is missing"})

#         dup_check = DataUseProcesses.objects.filter(id=dupId)
#         if not dup_check.exists():
#             return Response({'error': f"Data use process with the ID {dupId} does not exist."})

#         dup = DataUseProcesses.objects.get(id=dupId)

#         study_id = self.request.query_params.get('studyId')

#         if study_id is None:
#             return Response({'error': "studyId param is missing"})

#         study_check = Studies.objects.filter(id=study_id)
#         if not study_check.exists():
#             return Response({'error': f"Study with the ID {study_id} does not exist."})
#         study = Studies.objects.get(id=study_id)

#         dtp_studies_check = DtpStudies.objects.filter(study_id=study, dtp_id=dtp)
#         dup_studies_check = DupStudies.objects.filter(study_id=study, dup_id=dup)

#         data = {
#             "DtpTotal": dtp_studies_check.count(),
#             "DupTotal": dup_studies_check.count(),
#         }

#         study_objects_check = DataObjects.objects.filter(linked_study=study)
#         if not study_objects_check.exists():
#             return Response(data)

#         for rec in study_objects_check:
#             data_obj = DataObjects.objects.get(id=rec.id)
#             dtp_objects_check = DtpObjects.objects.filter(data_object=data_obj, dtp_id=dtp)
#             dup_objects_check = DupObjects.objects.filter(data_object=data_obj, dup_id=dup)
#             if dup_objects_check.exists():
#                 data['DupTotal'] += dup_objects_check.count()

#             if dtp_objects_check.exists():
#                 data['DtpTotal'] += dtp_objects_check.count()

#         return Response(data)


class NewMdrStudies(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        reg_id = self.request.query_params.get('regId')
        sd_sid = self.request.query_params.get('sdSid')

        if reg_id is None:
            return Response({'error': "regId param is missing"})
        if sd_sid is None:
            return Response({'error': "sdSid param is missing"})

        REG_IDS = [
            100116,
            100117,
            100118,
            100119,
            100120,
            100121,
            100122,
            100123,
            100124,
            100125,
            100126,
            100127,
            100128,
            100129,
            100130,
            100131,
            100132,
            100135,
            101405,
            101900,
            101901,
            101940,
            101989,
            109108,
            110426
        ]

        if int(reg_id) not in REG_IDS:
            return Response({'error': "Trial registry does not exist"})

        res = requests.get(
            f"https://newmdr.ecrin.org/api/Study/MDRId/{reg_id}/{sd_sid}",
        )
        study_id = res.text

        if study_id == "0" or study_id is None:
            return Response({'error': "Study does not exist"})

        study_details = requests.get(f"https://newmdr.ecrin.org/api/Study/StudyDetails/{study_id}")
        json_res = json.loads(study_details.text)

        study_type = None
        if 'study_type' in json_res:
            if json_res['study_type'] is not None:
                study_type_check = StudyTypes.objects.filter(name=json_res['study_type']['name'])
                if study_type_check.exists():
                    study_type = StudyTypes.objects.get(name=json_res['study_type']['name'])

        study_status = None
        if 'study_status' in json_res:
            if json_res['study_status'] is not None:
                study_status_check = StudyStatuses.objects.filter(name=json_res['study_status']['name'])
                if study_status_check.exists():
                    study_status = StudyStatuses.objects.get(name=json_res['study_status']['name'])

        study_gender_elig = None
        if 'study_gender_elig' in json_res:
            if json_res['study_gender_elig'] is not None:
                study_gender_elig_check = GenderEligibilityTypes.objects.filter(name=json_res['study_gender_elig']['name'])
                if study_gender_elig_check.exists():
                    study_gender_elig = GenderEligibilityTypes.objects.get(name=json_res['study_gender_elig']['name'])

        min_age_unit = None
        min_age_value = None
        if 'min_age' in json_res:
            if json_res['min_age'] is not None:
                min_age_unit_check = TimeUnits.objects.filter(name=json_res['min_age']['unit_name'])
                if min_age_unit_check.exists():
                    min_age_unit = TimeUnits.objects.get(name=json_res['min_age']['unit_name'])
                    min_age_value = int(json_res['min_age']['value'])

        max_age_unit = None
        max_age_value = None
        if 'max_age' in json_res:
            if json_res['max_age'] is not None:
                max_age_unit_check = TimeUnits.objects.filter(name=json_res['max_age']['unit_name'])
                if max_age_unit_check.exists():
                    max_age_unit = TimeUnits.objects.get(name=json_res['max_age']['unit_name'])
                    max_age_value = int(json_res['max_age']['value'])

        study = Studies(
            display_title=json_res['display_title'] if 'display_title' in json_res else 'Blank title',
            brief_description=json_res['brief_description'] if 'brief_description' in json_res else None,
            data_sharing_statement=json_res['data_sharing_statement'] if 'data_sharing_statement' in json_res else None,
            study_start_year=json_res['study_start_year'] if 'study_start_year' in json_res else None,
            study_start_month=json_res['study_start_month'] if 'study_start_month' in json_res else None,
            study_type=study_type,
            study_status=study_status,
            study_enrollment=json_res['study_enrollment'] if 'study_enrollment' in json_res else None,
            study_gender_elig=study_gender_elig,
            min_age=min_age_value,
            min_age_unit=min_age_unit,
            max_age=max_age_value,
            max_age_unit=max_age_unit,
        )
        study.save()

        serializer = StudiesOutputSerializer(study, many=False)

        return Response(serializer.data)


class StudiesByTitle(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        title_query_string = self.request.query_params.get('title')

        if title_query_string is None:
            return Response({'error': "title param is missing"})

        studies = Studies.objects.filter(display_title__icontains=title_query_string)

        serializer = StudiesLimitedOutputSerializer(studies, many=True)

        return Response(serializer.data)


class DataObjectsByTitle(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        title_query_string = self.request.query_params.get('title')

        if title_query_string is None:
            return Response({'error': "title param is missing"})

        data_objects = DataObjects.objects.filter(display_title__icontains=title_query_string)
        serializer = DataObjectsLimitedOutputSerializer(data_objects, many=True)

        return Response(serializer.data)


# class DtpByTitle(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
#     permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

#     def get(self, request):
#         title_query_string = self.request.query_params.get('title')

#         if title_query_string is None:
#             return Response({'error': "title param is missing"})

#         dtps = DataTransferProcesses.objects.filter(display_name__icontains=title_query_string)
#         serializer = DataTransferProcessesOutputSerializer(dtps, many=True)

#         return Response(serializer.data)


# class DupByTitle(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
#     permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

#     def get(self, request):
#         title_query_string = self.request.query_params.get('title')

#         if title_query_string is None:
#             return Response({'error': "title param is missing"})

#         dups = DataUseProcesses.objects.filter(display_name__icontains=title_query_string)
#         serializer = DataUseProcessesOutputSerializer(dups, many=True)

#         return Response(serializer.data)


class StudiesByTitleAndOrg(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        title_query_string = self.request.query_params.get('title')
        org_id = self.request.query_params.get('orgId')

        if org_id is None:
            return Response({'error': 'orgId param is missing'})

        org_check = Organisations.objects.filter(id=org_id)
        if not org_check.exists():
            return Response({'error': f'Organisation with the ID {org_id} does not exist'})

        org_data = Organisations.objects.get(id=org_id)

        if title_query_string is None:
            return Response({'error': "title param is missing"})

        studies = Studies.objects.filter(display_title__icontains=title_query_string, organisation=org_data)
        serializer = StudiesLimitedOutputSerializer(studies, many=True)

        return Response(serializer.data)


class DataObjectsByTitleAndOrg(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        title_query_string = self.request.query_params.get('title')
        org_id = self.request.query_params.get('orgId')

        if org_id is None:
            return Response({'error': 'orgId param is missing'})

        org_check = Organisations.objects.filter(id=org_id)
        if not org_check.exists():
            return Response({'error': f'Organisation with the ID {org_id} does not exist'})

        org_data = Organisations.objects.get(id=org_id)

        if title_query_string is None:
            return Response({'error': "title param is missing"})

        data_objects = DataObjects.objects.filter(display_title__icontains=title_query_string, organisation=org_data)
        serializer = DataObjectsLimitedOutputSerializer(data_objects, many=True)

        return Response(serializer.data)


# class DtpByTitleAndOrg(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
#     permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

#     def get(self, request):
#         title_query_string = self.request.query_params.get('title')
#         org_id = self.request.query_params.get('orgId')

#         if org_id is None:
#             return Response({'error': 'orgId param is missing'})

#         org_check = Organisations.objects.filter(id=org_id)
#         if not org_check.exists():
#             return Response({'error': f'Organisation with the ID {org_id} does not exist'})

#         org_data = Organisations.objects.get(id=org_id)

#         if title_query_string is None:
#             return Response({'error': "title param is missing"})

#         dtps = DataTransferProcesses.objects.filter(display_name__icontains=title_query_string, organisation=org_data)
#         serializer = DataTransferProcessesOutputSerializer(dtps, many=True)

#         return Response(serializer.data)


# class DupByTitleAndOrg(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
#     permission_classes = [permissions.IsAuthenticated & (IsSuperUser | ReadOnly)]

#     def get(self, request):
#         title_query_string = self.request.query_params.get('title')
#         org_id = self.request.query_params.get('orgId')

#         if org_id is None:
#             return Response({'error': 'orgId param is missing'})

#         org_check = Organisations.objects.filter(id=org_id)
#         if not org_check.exists():
#             return Response({'error': f'Organisation with the ID {org_id} does not exist'})

#         org_data = Organisations.objects.get(id=org_id)

#         if title_query_string is None:
#             return Response({'error': "title param is missing"})

#         dups = DataUseProcesses.objects.filter(display_name__icontains=title_query_string, organisation=org_data)
#         serializer = DataUseProcessesOutputSerializer(dups, many=True)

#         return Response(serializer.data)

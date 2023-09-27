import json

import requests
from mozilla_django_oidc.contrib.drf import OIDCAuthentication
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication


class MdrStudiesData(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication, OIDCAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        reg_id = self.request.query_params.get('regId')
        sd_sid = self.request.query_params.get('sdSid')

        if reg_id is None:
            return Response("regId param is missing")
        if sd_sid is None:
            return Response("sdSid param is missing")

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
            return Response("regId param is missing")
        if sd_sid is None:
            return Response("sdSid param is missing")

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
            return Response("mdrId param is missing")
        if sd_sid is None:
            return Response("sdSid param is missing")

        res = requests.get(
            f"https://api.ecrin-rms.org/api/data-objects/mdr/{sd_sid}/{mdr_id}",
            headers={'Authorization': request.META['HTTP_AUTHORIZATION']}
        )
        json_res = json.loads(res.text)

        return Response(json_res)

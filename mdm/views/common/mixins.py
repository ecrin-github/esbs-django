from django.shortcuts import get_object_or_404
from django.core.exceptions import FieldError
from django.http import HttpResponseForbidden
from rest_framework.response import Response

from rms.models import DataUseProcesses, DataTransferProcesses


class MultipleFieldLookupMixin:
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs.get(field): # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj


class ParentMultipleFieldLookupMixin:
    """
    Apply this mixin to any nested view or viewset to get multiple field filtering on the parent class.
    This class requires defining a `parent_lookup_fields` attribute for the filtering,
    a `fk_lookup_field` attribute which is the foreign key field name of the parent class in the child class,
    and a 'parent_queryset' attribute, which is all the objects (queryset) of the parent class.
    """
    def get_parent_object(self):
        parent_queryset = self.parent_queryset
        filter = {}
        for field in self.parent_lookup_fields:
            if self.kwargs.get(field): # Ignore empty fields.
                filter[self.parent_lookup_fields[field]] = self.kwargs[field]
        obj = get_object_or_404(parent_queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj
    
    def get_queryset(self, *args, **kwargs):
        if getattr(self, 'swagger_fake_view', False):
            # queryset just for schema generation metadata
            return self.object_class.objects.none()
        return (
            super()
            .get_queryset(*args, **kwargs)
            .filter(**{self.fk_lookup_field: self.get_parent_object().id})
        )


class GetAuthFilteringMixin:
    """
    Proper filtering of GET requests where users should only see items from their organisations, or none if they don't have an org
    This class requires defining an "object_class", the "queryset", and the "serializer" class variables
    """
    def get_dtp_dup_id(self, obj):
        return obj.id

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
            organisation = user.user_profile.organisation.id
            if hasattr(self.object_class, 'organisation'):
                return (
                    super()
                    .get_queryset(*args, **kwargs)
                    .filter(organisation=organisation)
                )
            elif hasattr(self.object_class, 'dtp_id'):
                # Class is sub-component of DTP class, need to test organisation on DTP
                dtp_id_set = set(map(self.get_dtp_dup_id, DataTransferProcesses.objects.filter(organisation=organisation)))
                return (
                    super()
                    .get_queryset(*args, **kwargs)
                    .filter(dtp_id__in=dtp_id_set)
                )
            elif hasattr(self.object_class, 'dup_id'):
                # Class is sub-component of DUP class, need to test organisation on DUP
                dup_id_set = set(map(self.get_dtp_dup_id, DataUseProcesses.objects.filter(organisation=organisation)))
                return (
                    super()
                    .get_queryset(*args, **kwargs)
                    .filter(dup_id__in=dup_id_set)
                )
        return self.object_class.objects.none()
    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except Exception:
            return HttpResponseForbidden('You do not have permission to perform this action.')
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
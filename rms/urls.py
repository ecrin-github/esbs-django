from django.urls import path

from rms.views.dtp.views import *
from rms.views.dup.views import *


dta_list = DataTransferAccessesList.as_view({
    'get': 'list',
    'post': 'create'
})
dta_detail = DataTransferAccessesList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

dtp_datasets_list = DtpDatasetsList.as_view({
    'get': 'list',
    'post': 'create'
})
dtp_datasets_detail = DtpDatasetsList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

dtp_notes_list = DtpNotesList.as_view({
    'get': 'list',
    'post': 'create'
})
dtp_notes_detail = DtpNotesList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

dtp_objects_list = DtpObjectsList.as_view({
    'get': 'list',
    'post': 'create'
})
dtp_objects_detail = DtpObjectsList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

dtp_people_list = DtpPeopleList.as_view({
    'get': 'list',
    'post': 'create'
})
dtp_people_detail = DtpPeopleList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

dtp_prereqs_list = DtpPrereqsList.as_view({
    'get': 'list',
    'post': 'create'
})
dtp_prereqs_detail = DtpPrereqsList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

dtp_studies_list = DtpStudiesList.as_view({
    'get': 'list',
    'post': 'create'
})
dtp_studies_detail = DtpStudiesList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

dtp_list = DataTransferProcessesList.as_view({
    'get': 'list',
    'post': 'create'
})
dtp_detail = DataTransferProcessesList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

dua_list = DataUseAccessesList.as_view({
    'get': 'list',
    'post': 'create'
})
dua_detail = DataUseAccessesList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

dup_notes_list = DupNotesList.as_view({
    'get': 'list',
    'post': 'create'
})
dup_notes_detail = DupNotesList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

dup_objects_list = DupObjectsList.as_view({
    'get': 'list',
    'post': 'create'
})
dup_objects_detail = DupObjectsList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

dup_people_list = DupPeopleList.as_view({
    'get': 'list',
    'post': 'create'
})
dup_people_detail = DupPeopleList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

dup_prereqs_list = DupPrereqsList.as_view({
    'get': 'list',
    'post': 'create'
})
dup_prereqs_detail = DupPrereqsList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

dup_secondary_use_list = DupSecondaryUseList.as_view({
    'get': 'list',
    'post': 'create'
})
dup_secondary_use_detail = DupSecondaryUseList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

dup_studies_list = DupStudiesList.as_view({
    'get': 'list',
    'post': 'create'
})
dup_studies_detail = DupStudiesList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

dup_list = DataUseProcessesList.as_view({
    'get': 'list',
    'post': 'create'
})
dup_detail = DataUseProcessesList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('dtp/<uuid:dtpId>/dta', dta_list),
    path('dtp/<uuid:dtpId>/dta/<uuid:pk>', dta_detail),

    path('dtp/<uuid:dtpId>/datasets', dtp_datasets_list),
    path('dtp/<uuid:dtpId>/datasets/<uuid:pk>', dtp_datasets_detail),

    path('dtp/<uuid:dtpId>/notes', dtp_notes_list),
    path('dtp/<uuid:dtpId>/notes/<uuid:pk>', dtp_notes_detail),

    path('dtp/<uuid:dtpId>/objects', dtp_objects_list),
    path('dtp/<uuid:dtpId>/objects/<uuid:pk>', dtp_objects_detail),

    path('dtp/<uuid:dtpId>/people', dtp_people_list),
    path('dtp/<uuid:dtpId>/people/<uuid:pk>', dtp_people_detail),

    path('dtp/<uuid:dtpId>/prereqs', dtp_prereqs_list),
    path('dtp/<uuid:dtpId>/prereqs/<uuid:pk>', dtp_prereqs_detail),

    path('dtp/<uuid:dtpId>/studies', dtp_studies_list),
    path('dtp/<uuid:dtpId>/studies/<uuid:pk>', dtp_studies_detail),

    path('dtp', dtp_list),
    path('dtp/<uuid:pk>', dtp_detail),

    path('dup/<uuid:dupId>/dua', dua_list),
    path('dup/<uuid:dupId>/dua/<uuid:pk>', dua_detail),

    path('dup/<uuid:dupId>/notes', dup_notes_list),
    path('dup/<uuid:dupId>/notes/<uuid:pk>', dup_notes_detail),

    path('dup/<uuid:dupId>/objects', dup_objects_list),
    path('dup/<uuid:dupId>/objects/<uuid:pk>', dup_objects_detail),

    path('dup/<uuid:dupId>/people', dup_people_list),
    path('dup/<uuid:dupId>/people/<uuid:pk>', dup_people_detail),

    path('dup/<uuid:dupId>/prereqs', dup_prereqs_list),
    path('dup/<uuid:dupId>/prereqs/<uuid:pk>', dup_prereqs_detail),

    path('dup/<uuid:dupId>/secondary-use', dup_secondary_use_list),
    path('dup/<uuid:dupId>/secondary-use/<uuid:pk>', dup_secondary_use_detail),

    path('dup/<uuid:dupId>/studies', dup_studies_list),
    path('dup/<uuid:dupId>/studies/<uuid:pk>', dup_studies_detail),

    path('dup', dup_list),
    path('dup/<uuid:pk>', dup_detail),
]

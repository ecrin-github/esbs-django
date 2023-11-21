from django.urls import path

from users.views.views import *

users_list = UsersList.as_view({
    'get': 'list',
    'post': 'create'
})
users_detail = UsersList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_profiles_detail = UserProfilesList.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = [
    path('', users_list),
    path('<uuid:pk>', users_detail),

    path('<uuid:userId>/profile/<uuid:pk>', user_profiles_detail),

    path('<uuid:userId>/entities', UserEntitiesApiView.as_view()),

    path('by-org', UsersByOrganisation.as_view())
]

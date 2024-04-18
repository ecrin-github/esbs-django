from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="The ESBS API",
      default_version='v1',
      description="Test ECRIN System Back-end Services API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="frequenteen@gmail.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls', namespace='rest_framework')),

    path('oidc/', include('mozilla_django_oidc.urls')),

    path('app/', include('app.urls')),

    path('api/context/', include('context.urls')),
    path('api/general/', include('general.urls')),
    path('api/mdm/', include('mdm.urls')),
    path('api/rms/', include('rms.urls')),
    path('api/users/', include('users.urls')),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

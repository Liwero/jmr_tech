from typing import ChainMap
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication
schema_view = get_schema_view(
   openapi.Info(
      title="JMR API",
      default_version='v1',
   ),
   public=True,
   authentication_classes=(BasicAuthentication,),
   permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("v1/", include("jmr_app.urls")),
]

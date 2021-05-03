from django.urls import include, path
from rest_framework.routers import DefaultRouter

from jmr_app.views import RedirectURLViewSet

router = DefaultRouter()
router.register("jmr", RedirectURLViewSet, basename="jmr")

urlpatterns = [
    path("", include(router.urls))
]
from django.http import HttpResponseRedirect
from rest_framework.viewsets import ModelViewSet

from jmr_app.models import RedirectURL
from jmr_app.serializers import RedirectURLSerializer


class RedirectURLViewSet(ModelViewSet):
    authentication_classes = []
    queryset = RedirectURL.objects.all()
    serializer_class = RedirectURLSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return HttpResponseRedirect(instance.original_url)

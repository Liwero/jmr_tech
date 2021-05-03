from rest_framework.serializers import ModelSerializer, SerializerMethodField

from jmr_app.models import RedirectURL


class RedirectURLSerializer(ModelSerializer):
    redirect_url = SerializerMethodField(read_only=True)
    class Meta:
        model = RedirectURL
        fields = ("original_url", "redirect_url")

    def get_redirect_url(self, obj):
        return self.context["request"].build_absolute_uri(obj.pk)
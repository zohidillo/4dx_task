from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import RetrieveAPIView

import src.core.models as models
import src.apps.serializers as serializers


class DetailBusinessPartnerApiView(RetrieveAPIView, GenericViewSet):
    queryset = models.BusinessPartner.objects.select_related("created_by", "updated_by")
    serializer_class = serializers.DetailBusinessPartnerSerializer

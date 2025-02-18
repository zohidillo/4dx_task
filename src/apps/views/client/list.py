from rest_framework.generics import ListAPIView
from rest_framework.viewsets import GenericViewSet

import src.core.models as models
import src.apps.serializers as serializers


class ListBusinessPartnerAPIView(ListAPIView, GenericViewSet):
    queryset = models.BusinessPartner.objects.all()
    serializer_class = serializers.ListBusinessPartnerSerializer

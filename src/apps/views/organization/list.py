from rest_framework.generics import ListAPIView
from rest_framework.viewsets import GenericViewSet

import src.core.models as models
import src.apps.serializers as serializers


class ListOrganizationAPIView(ListAPIView, GenericViewSet):
    queryset = models.Organization.objects.select_related("measurement")
    serializer_class = serializers.ListOrganizationSerializer

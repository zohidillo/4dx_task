from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import RetrieveAPIView

import src.core.models as models
import src.apps.serializers as serializers


class DetailOrganizationApiView(RetrieveAPIView, GenericViewSet):
    queryset = models.Organization.objects.select_related("created_by", "updated_by")
    serializer_class = serializers.DetailOrganizationSerializer

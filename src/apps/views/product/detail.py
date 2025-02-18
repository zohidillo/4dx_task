from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import RetrieveAPIView

import src.core.models as models
import src.apps.serializers as serializers


class DetailProductApiView(RetrieveAPIView, GenericViewSet):
    queryset = models.Product.objects.select_related("measurement", "created_by", "updated_by")
    serializer_class = serializers.DetailProductSerializer

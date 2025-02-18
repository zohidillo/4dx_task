from rest_framework.generics import ListAPIView
from rest_framework.viewsets import GenericViewSet

import src.core.models as models
import src.apps.serializers as serializers


class ListProductAPIView(ListAPIView, GenericViewSet):
    queryset = models.Product.objects.select_related("measurement")
    serializer_class = serializers.ListProductSerializer

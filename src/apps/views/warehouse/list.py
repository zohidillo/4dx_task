from rest_framework.generics import ListAPIView
from rest_framework.viewsets import GenericViewSet

import src.core.models as models
import src.apps.serializers as serializers


class ListWarehouseAPIView(ListAPIView, GenericViewSet):
    queryset = models.Warehouse.objects.all()
    serializer_class = serializers.ListWarehouseSerializer

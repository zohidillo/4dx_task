from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import RetrieveAPIView

import src.core.models as models
import src.apps.serializers as serializers


class DetailDocumentSaleApiView(RetrieveAPIView, GenericViewSet):
    queryset = models.DocumentSale.objects.select_related("created_by", "updated_by", "client",
                                                          "organization").prefetch_related("items")
    serializer_class = serializers.DetailDocumentSaleSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from rest_framework.viewsets import GenericViewSet

from decimal import Decimal
from django.db import transaction

import src.core.models as models
import src.apps.serializers as serializers


class UpdateDocumentSaleApiView(UpdateAPIView, GenericViewSet):
    queryset = models.DocumentSale.objects.select_related(
        "created_by", "client", "organization").prefetch_related("items")
    serializer_class = serializers.UpdateDocumentSaleSerializer

    def update(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        instance = self.get_object()
        items = data.pop("items", [])

        try:
            with transaction.atomic():
                instance.client_id = data.get("client", instance.client_id)
                instance.organization_id = data.get("organization", instance.organization_id)
                instance.updated_by = user

                items_list = []
                total = Decimal(0.00)
                if items:
                    for i in items:
                        quantity = i.get("quantity")
                        if quantity is None:
                            return Response(
                                {"error": "'quantity' This field is required"},
                                status=status.HTTP_400_BAD_REQUEST
                            )

                        sale_price = i.get("sale_price")
                        if sale_price is None:
                            return Response(
                                {"error": "'sale_price' This field is required"},
                                status=status.HTTP_400_BAD_REQUEST
                            )

                        total_sale_price = Decimal(quantity) * Decimal(sale_price)
                        total += total_sale_price

                        item = models.DocumentSaleItem(
                            document=instance,
                            product_id=i.pop("product"),
                            warehouse_id=i.pop("warehouse"),
                            total_sale_price=total_sale_price,
                            quantity=quantity,
                            sale_price=sale_price,
                            purchase_price=i.get("purchase_price")
                        )
                        items_list.append(item)

                    instance.items.all().delete()
                    models.DocumentSaleItem.objects.bulk_create(items_list)
                    instance.total_sum = total
                    instance.save()

                saved_data = serializers.DetailDocumentSaleSerializer(instance).data
                return Response(saved_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

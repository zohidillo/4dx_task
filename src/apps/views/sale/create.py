from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import GenericViewSet

from decimal import Decimal
from django.db import transaction

import src.core.models as models
import src.apps.serializers as serializers


class CreateDocumentSaleApiView(CreateAPIView, GenericViewSet):
    queryset = models.DocumentSale.objects.select_related(
        "created_by", "client", "organization").prefetch_related("items")
    serializer_class = serializers.CreateDocumentSaleSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        items = data.pop("items", [])

        try:
            with transaction.atomic():
                obj = models.DocumentSale.objects.create(
                    created_by=user,
                    client_id=data.get("client"),
                    organization_id=data.get("organization")
                )
                items_list = []
                total = Decimal(0.00)

                for i in items:
                    quantity = i.get("quantity")
                    if quantity is None:
                        return Response(
                            {"error": "'quantity' This field is required"}, status=status.HTTP_400_BAD_REQUEST
                        )
                    sale_price = i.get("sale_price")
                    if sale_price is None:
                        return Response(
                            {"error": "'sale_price' This field is required"}, status=status.HTTP_400_BAD_REQUEST
                        )
                    total_sale_price = Decimal(quantity) * Decimal(sale_price)
                    total += total_sale_price
                    item = models.DocumentSaleItem(
                        document=obj,
                        product_id=i.pop("product"),
                        warehouse_id=i.pop("warehouse"),
                        total_sale_price=total_sale_price,
                        quantity=quantity,
                        sale_price=sale_price,
                        purchase_price=i.get("purchase_price")
                    )
                    items_list.append(item)
                models.DocumentSaleItem.objects.bulk_create(items_list)

                obj.total_sum = total
                obj.save()

                saved_data = serializers.DetailDocumentSaleSerializer(obj).data
                return Response(saved_data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)

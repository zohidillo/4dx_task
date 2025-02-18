from rest_framework import serializers

import src.core.models as models
import src.apps.serializers.sale.items as item


class CreateDocumentSaleSerializer(serializers.ModelSerializer):
    items = serializers.ListSerializer(child=item.CreateDocumentSaleItemSerializer())

    class Meta:
        model = models.DocumentSale
        fields = ("client", "organization", "items")

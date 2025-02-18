from rest_framework import serializers

import src.core.models as models
import src.apps.serializers.base as base


class CreateDocumentSaleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DocumentSaleItem
        fields = ("product", "quantity", "sale_price", "purchase_price", "warehouse")


class DocumentSaleItemSerializer(serializers.ModelSerializer):
    product = base.build_relational_model_serializer(models.Product, fields_=("id", "name"))
    warehouse = base.build_relational_model_serializer(models.Warehouse, fields_=("id", "name"))

    class Meta:
        model = models.DocumentSaleItem
        exclude = ("created_by", "updated_by", "added_at", "updated_at", "document")

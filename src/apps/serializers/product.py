from rest_framework import serializers

import src.core.models as models
import src.apps.serializers.base as base


class ListProductSerializer(serializers.ModelSerializer):
    measurement = base.build_relational_model_serializer(models.ProductMeasurement, fields_=("id", "name"))

    class Meta:
        model = models.Product
        fields = ("id", "name", "measurement", "product_code")


class DetailProductSerializer(base.BaseSerializer):
    measurement = base.build_relational_model_serializer(models.ProductMeasurement, fields_=("id", "name"))
    created_by = base.build_relational_model_serializer(models.User, fields_=("id", "username"))
    updated_by = base.build_relational_model_serializer(models.User, fields_=("id", "username"))

    class Meta:
        model = models.Product
        fields = "__all__"

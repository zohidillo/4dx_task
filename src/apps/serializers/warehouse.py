from rest_framework import serializers

import src.core.models as models
import src.apps.serializers.base as base


class ListWarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Warehouse
        fields = ("id", "name")


class DetailWarehouseSerializer(base.BaseSerializer):
    created_by = base.build_relational_model_serializer(models.User, fields_=("id", "username"))
    updated_by = base.build_relational_model_serializer(models.User, fields_=("id", "username"))

    class Meta:
        model = models.Warehouse
        fields = "__all__"

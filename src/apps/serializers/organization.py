from rest_framework import serializers

import src.core.models as models
import src.apps.serializers.base as base


class ListOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        fields = ("id", "name")


class DetailOrganizationSerializer(base.BaseSerializer):
    created_by = base.build_relational_model_serializer(models.User, fields_=("id", "username"))
    updated_by = base.build_relational_model_serializer(models.User, fields_=("id", "username"))

    class Meta:
        model = models.Organization
        fields = "__all__"

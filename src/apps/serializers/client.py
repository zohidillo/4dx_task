from rest_framework import serializers

import src.core.models as models
import src.apps.serializers.base as base


class ListBusinessPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BusinessPartner
        fields = ("id", "full_name", "client_code")


class DetailBusinessPartnerSerializer(base.BaseSerializer):
    created_by = base.build_relational_model_serializer(models.User, fields_=("id", "username"))
    updated_by = base.build_relational_model_serializer(models.User, fields_=("id", "username"))

    class Meta:
        model = models.BusinessPartner
        fields = "__all__"

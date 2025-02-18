import src.core.models as models
import src.apps.serializers.base as base


class DetailDocumentSaleSerializer(base.BaseSerializer):
    created_by = base.build_relational_model_serializer(models.User, fields_=("id", "username"))
    updated_by = base.build_relational_model_serializer(models.User, fields_=("id", "username"))

    class Meta:
        model = models.DocumentSale
        fields = "__all__"

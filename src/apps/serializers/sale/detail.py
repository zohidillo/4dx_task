import src.core.models as models
import src.apps.serializers.base as base
from src.apps.serializers.sale.items import DocumentSaleItemSerializer


class DetailDocumentSaleSerializer(base.BaseSerializer):
    client = base.build_relational_model_serializer(models.BusinessPartner, fields_=("id", "full_name"))
    organization = base.build_relational_model_serializer(models.Organization, fields_=("id", "name"))
    created_by = base.build_relational_model_serializer(models.User, fields_=("id", "username"))
    updated_by = base.build_relational_model_serializer(models.User, fields_=("id", "username"))
    items = DocumentSaleItemSerializer(many=True)

    class Meta:
        model = models.DocumentSale
        fields = "__all__"

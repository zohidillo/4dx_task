from src.core.models.base import *


class DocumentSale(BaseModel):
    client = models.ForeignKey("BusinessPartner", on_delete=models.SET_NULL, null=True, related_name="sales")
    organization = models.ForeignKey("Organization", on_delete=models.SET_NULL, null=True,
                                     related_name="organization_sales")
    total_sum = models.DecimalField(max_digits=16, decimal_places=2, null=True)

    class Meta:
        db_table = "document_sales"


class DocumentSaleItem(BaseModel):
    document = models.ForeignKey(DocumentSale, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True)
    quantity = models.DecimalField(max_digits=16, decimal_places=2)
    sale_price = models.DecimalField(max_digits=16, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=16, decimal_places=2)
    total_sale_price = models.DecimalField(max_digits=16, decimal_places=2)
    warehouse = models.ForeignKey("Warehouse", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "document_sale_items"

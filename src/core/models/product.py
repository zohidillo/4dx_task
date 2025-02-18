from src.core.models.base import *


class ProductMeasurement(BaseModel):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "product_measurements"


class Product(BaseModel):
    name = models.CharField(max_length=200)
    product_code = models.CharField(max_length=10)
    measurement = models.ForeignKey(ProductMeasurement, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "products"

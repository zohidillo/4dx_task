from src.core.models.base import *


class Warehouse(BaseModel):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "warehouses"

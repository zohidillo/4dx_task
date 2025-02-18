from src.core.models.base import *


class BusinessPartner(BaseModel):
    full_name = models.CharField(max_length=100)
    client_code = models.CharField(max_length=10)

    class Meta:
        db_table = "business_partners"

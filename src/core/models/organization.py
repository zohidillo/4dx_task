from src.core.models.base import *


class Organization(BaseModel):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "organizations"

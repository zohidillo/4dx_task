from django.contrib import admin

# Register your models here.
import src.core.models as models


@admin.register(models.ProductMeasurement)
class Admin(admin.ModelAdmin):
    pass


@admin.register(models.Product)
class Admin(admin.ModelAdmin):
    pass


@admin.register(models.BusinessPartner)
class Admin(admin.ModelAdmin):
    pass


@admin.register(models.Organization)
class Admin(admin.ModelAdmin):
    pass


@admin.register(models.Warehouse)
class Admin(admin.ModelAdmin):
    pass


@admin.register(models.DocumentSale)
class Admin(admin.ModelAdmin):
    pass


@admin.register(models.DocumentSaleItem)
class Admin(admin.ModelAdmin):
    pass

from django.urls import path, include

urlpatterns = [
    path("sale/", include("src.apps.urls.sale")),
    path("client/", include("src.apps.urls.client")),
    path("product/", include("src.apps.urls.product")),
    path("warehouse/", include("src.apps.urls.warehouse")),
    path("organization/", include("src.apps.urls.organization")),
]

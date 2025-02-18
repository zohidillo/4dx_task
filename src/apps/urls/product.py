from rest_framework.routers import SimpleRouter

from src.apps.views.product import *

router = SimpleRouter()
router.register("list", ListProductAPIView, basename="list-product")
router.register("detail", DetailProductApiView, basename="detail-product")

urlpatterns = [] + router.urls

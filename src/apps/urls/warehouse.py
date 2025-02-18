from rest_framework.routers import SimpleRouter

from src.apps.views.warehouse import *

router = SimpleRouter()
router.register("list", ListWarehouseAPIView, basename="list-warehouse")
router.register("detail", DetailWarehouseApiView, basename="detail-warehouse")

urlpatterns = [] + router.urls

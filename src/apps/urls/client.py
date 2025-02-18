from rest_framework.routers import SimpleRouter

from src.apps.views.client import *

router = SimpleRouter()
router.register("list", ListBusinessPartnerAPIView, basename="list-client")
router.register("detail", DetailBusinessPartnerApiView, basename="detail-client")

urlpatterns = [] + router.urls

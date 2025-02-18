from rest_framework.routers import SimpleRouter

from src.apps.views.organization import *

router = SimpleRouter()
router.register("list", ListOrganizationAPIView, basename="list-organization")
router.register("detail", DetailOrganizationApiView, basename="detail-organization")

urlpatterns = [] + router.urls

from rest_framework.routers import SimpleRouter

from src.apps.views.sale import *

router = SimpleRouter()
router.register("create", CreateDocumentSaleApiView, basename="create-document-sale")
router.register("update", UpdateDocumentSaleApiView, basename="update-document-sale")
router.register("detail", DetailDocumentSaleApiView, basename="detail-document-sale")

urlpatterns = [] + router.urls

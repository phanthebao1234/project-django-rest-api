from rest_framework.routers import DefaultRouter

from products.viewset import ProductViewSet, ProductGenericViewSet, ProductGenericViewSetv2

router = DefaultRouter()
router.register('product', ProductGenericViewSetv2, basename='products')


urlpatterns = router.urls
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from . import viewset

router = DefaultRouter()
router.register('', viewset.ProductGenericViewSet)

urlpatterns = [
    path('', include(router.urls))
    # path('', views.product_mixin_view, name='product-list'),
    # path('<int:pk>/', views.product_detail_view, name='product-detail'),
    # path('<int:pk>/update/', views.product_update_view, name='product-edit'),
    # path('<int:pk>/delete/', views.product_delete_view),
]
 

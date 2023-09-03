from django.urls import path
from . import views
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
product_router = routers.NestedDefaultRouter(
    router, parent_prefix="products", lookup='product')
product_router.register('reviews', views.ReviewViewSet,
                        basename='product-reviews')

carts_router = routers.NestedDefaultRouter(
    router, parent_prefix='carts', lookup='cart')

carts_router.register('items', views.CartItemsViewSet, basename='cart-items')

urlpatterns = router.urls + product_router.urls + carts_router.urls

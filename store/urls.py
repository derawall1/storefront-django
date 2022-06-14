from cgitb import lookup
from django.urls import include, path
from rest_framework_nested import routers


from .views import \
    ProductViewSet, CollectionViewSet, \
    ReviewViewSet, CartViewSet, \
    CartItemViewSet, CustomerViewSet, \
    OrderViewSet, ProductImageViewSet
#from pprint import pprint

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('collections', CollectionViewSet,  basename='collections')
router.register('reviews',ReviewViewSet,  basename='reivews')
router.register('carts', CartViewSet, basename='carts' )
router.register('customers', CustomerViewSet, basename='customers' )
router.register('orders', OrderViewSet, basename='orders' )
products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', ReviewViewSet, basename='product-reivews')
products_router.register('images', ProductImageViewSet, basename='product-images')

cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items',CartItemViewSet, basename='cart-items')

urlpatterns= router.urls + products_router.urls + cart_router.urls
# urlpatterns = [
#     path(r'', include(router.urls)),
#     path(r'', include(products_router.urls)),
# ]
#pprint(router.urls)
#URLConf
#urlpatterns= router.urls
# urlpatterns = [
#     path('products/',views.ProductList.as_view()),
#     path('products/<int:pk>/',views.ProductDetail.as_view()),
#     path('collections/',views.CollectionList.as_view(), name= 'collection-list'),
#     path('collections/<int:pk>/',views.CollectionDetail.as_view(), name= 'collection-detail'),

# ]
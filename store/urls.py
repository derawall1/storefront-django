from django.urls import include, path
from rest_framework_nested import routers
from .views import ProductViewSet, CollectionViewSet, ReviewViewSet
#from pprint import pprint

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('collections', CollectionViewSet,  basename='collections')
router.register('reviews',ReviewViewSet,  basename='reivews')
products_router = routers.NestedDefaultRouter(router, r'products', lookup='product')
products_router.register(r'reviews', ReviewViewSet, basename='product-reivews')
urlpatterns= router.urls + products_router.urls
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
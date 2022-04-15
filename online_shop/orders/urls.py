from django.urls import path, include
from rest_framework.routers import DefaultRouter

from orders.apis import OrderViewSet, OrderItemViewSet, OrderItemOfProduct, AfterOffCodeApiView
from orders.views import NotLoginHandler, OrderItemListView, OrderCreateView

router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'order_items', OrderItemViewSet)

app_name = 'orders'
urlpatterns = [
    path('', include(router.urls)),
    path('order_item_of_product', OrderItemOfProduct.as_view(), name='order_item_of_product'),
    path('not_login_handler', NotLoginHandler.as_view(), name='not_login_handler'),
    path('order_items_list', OrderItemListView.as_view(), name='order_items_list'),
    path('order_create', OrderCreateView.as_view(), name='order_create'),
    path('after_off_code_api', AfterOffCodeApiView.as_view(), name='after_off_code_api'),
]

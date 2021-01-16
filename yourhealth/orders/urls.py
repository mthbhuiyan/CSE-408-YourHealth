from django.conf.urls import url

from .views import order_create, OrderListView

app_name = 'orders'

urlpatterns = [
    url(r'^create/$', order_create, name='order_create'),
    url(r'^list/$', OrderListView.as_view(), name='order_list'),
]

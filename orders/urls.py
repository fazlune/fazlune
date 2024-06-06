from django.urls import path
from .views import create_order, orders_for_user_page, orders_for_admin_page

app_name = 'orders'
urlpatterns = [
    path('create-order/<slug:slug>', create_order, name='create_order'),
    path('all_orders/', orders_for_admin_page, name='all-orders'),
    path('my_orders/', orders_for_user_page, name='my-orders'),
]
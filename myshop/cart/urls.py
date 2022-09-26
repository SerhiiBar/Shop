from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', CartDetail.as_view(), name='cart_detail'),
    path('<product_id>/', views.cart_add, name='cart_add'),
    path('<product_id>', views.cart_remove, name='cart_remove'),

]

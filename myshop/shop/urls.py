from django.urls import path

from .views import *


urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('product/<slug:product_slug>/', ProductDetail.as_view(), name='product_detail'),
    path('category/<slug:category_slug>/', CategoryView.as_view(), name='category')
]

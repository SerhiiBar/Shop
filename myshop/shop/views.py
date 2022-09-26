from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.decorators.http import require_POST
from .models import *
from cart.cart import Cart
from cart.forms import CartAddProductForm


class ProductList(ListView):
    model = Product
    template_name = 'shop/products/list.html'
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CategoryView(ListView):
    model = Product
    template_name = 'shop/products/list.html'
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category__slug=self.kwargs['category_slug'])
        context['categories'] = Category.objects.all()
        context['category'] = Category.objects.filter(slug=self.kwargs['category_slug'])[0]
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'shop/products/detail.html'
    slug_url_kwarg = 'product_slug'
    context_object_name = 'product'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['cart_product_form'] = CartAddProductForm()
        return context


# @require_POST
# def cart_add(request, product_id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=product_id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product,
#                  quantity=cd['quantity'],
#                  update_quantity=cd['update'])
#     return redirect('cart:cart_detail')

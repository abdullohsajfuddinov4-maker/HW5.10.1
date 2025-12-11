from django.shortcuts import render
from django.views.generic import ListView , DetailView ,CreateView
from .models import Product
# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'product'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail.html'
    context_object_name = 'product'


# class ProductCreateView(CreateView):


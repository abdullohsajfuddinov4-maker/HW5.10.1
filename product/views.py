from django.shortcuts import render
from django.views.generic import ListView , DetailView ,CreateView ,UpdateView ,DeleteView
from .models import Product
from .forms import ProductForm
from django.urls import reverse_lazy
# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'product'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'create.html'
    success_url = reverse_lazy('home')


class ProductUpdate(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'update.html'
    success_url = reverse_lazy('home')


class ProductDelete(DeleteView):
    model = Product
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


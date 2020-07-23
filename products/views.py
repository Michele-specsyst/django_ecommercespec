<<<<<<< HEAD
from django.views.generic import ListView, DetailView
from django.shortcuts import render
=======
from django.views.generic import ListView,DetailView
from django.shortcuts import render, get_object_or_404
>>>>>>> 1d23f35148ef7c5465d75f970b4fffa81f8e9948

from .models import Product


# Class Based View
class ProductListView(ListView):
    # traz todos os produtos do banco de dados sem filtrar nada
    queryset = Product.objects.all()
    template_name = "products/list.html"

    #def get_context_data(self, *args, **kwargs):
    #   context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #   print(context)
    #   return context


# Class Based View
class ProductDetailView(DetailView):
    # traz todos os produtos do banco de dados sem filtrar nada
    queryset = Product.objects.all()
    template_name = "products/detail.html"

<<<<<<< HEAD
    # def get_context_data(self, *args, **kwargs):
    # context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
    # print(context)
    # return context
=======
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
>>>>>>> 1d23f35148ef7c5465d75f970b4fffa81f8e9948

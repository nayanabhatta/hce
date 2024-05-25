from django.shortcuts import render

# Create your views here.
#categories/views.py
from poducts.models import Poducts
from .serializers import CategorySerializer
from rest_framework import generics
from rest_framework.filters import SearchFilter
from .models import Category

def category_list(request):
    categories = Category.objects.all() #retrieve all categories
    print(categories)
    return render(request, 'categories/category_list.html',{'categories': categories})

def category_poducts(request):
    categories = Category.objects.all()
    poducts = Poducts.objects.all()
    return render(request, 'categories/category_poducts.html',{'categories':categories,'poducts':poducts})

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name','description']

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Category.objects.all() 
    serializer_class = CategorySerializer   

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from django.contrib.auth.decorators import login_required

from .models import *
from .filters import *

def index(request):
    return render(request, 'spare/index.html')

def about(request):
    return render(request, 'spare/about.html')

def home(request):
    products = Product.objects.all().order_by('-id')
    product_filters = ProductFilter(request.GET,queryset = products)
#Query set
    products = product_filters.qs 
    return render(request,'spare/home.html', {'products': products, 'product_filters': product_filters})
    
@login_required
def product_detail(request, id):
    product = Product.objects.get(id == id)
    return render(request,'spare/product_detail.html',{'product':product})
    



def product_detail(request):
    pass
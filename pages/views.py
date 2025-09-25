from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#    return HttpResponse("<h1>Hello World!</h1>")

def index(request):
    return render(request, 'pages/index.html')

def products(request):
    return render(request, 'pages/products.html')

def about(request):
    return render(request, 'pages/about.html')

from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing

# Create your views here.

# def index(request):
#    return HttpResponse("<h1>Hello World!</h1>")

def index(request):
    listings = Listing.objects.filter(is_published=True)[:3] # Get the 3 most recent published listings
    context={'listings': listings}
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def test(request):
    # print(request.path)
    # print(request)
    return render(request, 'pages/test.html')
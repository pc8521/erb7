from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from doctors.models import Doctor

# Create your views here.

# def index(request):
#    return HttpResponse("<h1>Hello World!</h1>")

def index(request):
    listings = Listing.objects.filter(is_published=True)[:3] # Get the 3 most recent published listings
    context={'listings': listings}
    return render(request, 'pages/index.html', context)

def about(request):
    doctors = Doctor.objects.order_by('-hire_date')[:3] # Get the 3 most recent doctors
    mvp_doctor = Doctor.objects.all().filter(is_mvp=True) # Get the MVP doctor
    context={'doctors': doctors, 'mvp_doctor': mvp_doctor}
    return render(request, 'pages/about.html', context)

def test(request):
    # print(request.path)
    # print(request)
    return render(request, 'pages/test.html')
from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

# def index(request):
#    return HttpResponse("<h1>Hello World!</h1>")

def listings(request):
    # listings=Listing.objects.all()
    #QuerySet of published listings
    listings=Listing.objects.order_by('list_date').filter(is_published=True)
    paginator=Paginator(listings, 3) # Show 3 listings per page
    page=request.GET.get('page')
    paged_listings=paginator.get_page(page)
    context={'listings': paged_listings}
    return render(request, 'listings/listings.html', context)
    # return render(request, 'listings/listings.html', {'name': 'Medical Center Listings'})  

def listing(request, listing_id):
    listing=Listing.objects.get(id=listing_id)
    context={'listing': listing}
    return render(request, 'listings/listing.html', context)

def search(request):
    return render(request, 'listings/search.html')
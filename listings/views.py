from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Listing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from listings.choices import district_choices, room_choices, night_choices

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
    # listing=Listing.objects.get(id=listing_id)
    listing=get_object_or_404(Listing, pk=listing_id)
    context={'listing': listing}
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list=Listing.objects.order_by('-list_date')
    if 'keywords' in request.GET:
        keywords=request.GET['keywords']
        if keywords:
            queryset_list=queryset_list.filter(description__icontains=keywords)
    if 'district' in request.GET:
        district=request.GET['district']
        if district:
            queryset_list=queryset_list.filter(district__iexact=district)
    if 'nights' in request.GET:
        nights=request.GET['nights']
        if nights:
            queryset_list=queryset_list.filter(nights__lte=nights)
    if 'room_type' in request.GET:
        room_type=request.GET['room_type']
        if room_type:
            queryset_list=queryset_list.filter(room_type__iexact=room_type)
    context={
        'listings': queryset_list,
        'district_choices': district_choices,
        'night_choices': night_choices,
        'room_choices': room_choices,
        'values': request.GET
    }
    return render(request, 'listings/search.html' , context)
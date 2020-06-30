from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import bedroom_choices, state_choices, price_choices

#Load Model
from .models import Listing

# Create your views here.

#All List
def index(request):
    #listings = Listing.objects.all()
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    #Pagination Techniques
    paginator = Paginator(listings, 10)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    context = {
        'listings' : page_listings
    }
    return render(request, 'listings/listings.html', context)


#Single Item From The List
def listing(request, listing_id):
    #Django 404 Default Page Genarators
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


#For Search
def search(request):

    queryset_list = Listing.objects.order_by('-list_date')

    #Keyword
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
            #icontains= Mach at lest a charecter
    #City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
            #iexact = Exact Same

    #State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
            #iexact = Exact Same

    #Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
            #lte = Lessthan or Equal To




    #Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
            #lte = Lessthan or Equal To


    context = {
        'bedroom_choices' : bedroom_choices,
        'state_choices' : state_choices,
        'price_choices' : price_choices,
        'queryset_list' : queryset_list,
        'values' : request.GET
    }

    return render(request, 'listings/search.html', context)

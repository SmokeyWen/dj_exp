from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing
from listings.choices import author_choice, price_choice, duration_choice

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-complete_date')
    paginator = Paginator(listings, 9)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    query_list = Listing.objects.order_by('-complete_date')

    #filter with title keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_list = query_list.filter(title__icontains = keywords)

    #filter with author dropdown
    #searching with foreign key of the listing table
    if 'author' in request.GET:
        author = request.GET['author']
        if author:
            query_list = query_list.filter(author__name__icontains = author)

    #filter with initial price. naming changed between select and db column name
    if 'price' in request.GET:
        initial_price = request.GET['price']
        if initial_price:
            query_list = query_list.filter(initial_price__lte = initial_price)

    #filter with number of days. naming changed with db column name
    if 'days' in request.GET:
        duration = request.GET['days']
        if duration:
            query_list = query_list.filter(duration__lte = duration)



    context = {
        'author_choice': author_choice,
        'price_choice': price_choice,
        'duration_choice': duration_choice,
        'results': query_list
    }
    return render(request, 'listings/search.html', context)
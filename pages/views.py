from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from authors.models import Author

def index(request):
    listings = Listing.objects.order_by('-complete_date')[:3]
    context = {
        'listings': listings
    }
    return render(request, 'pages/index.html', context)

def about(request):
    authors = Author.objects.order_by('id')
    context = {
        'authors': authors
    }
    return render(request, 'pages/about.html', context)
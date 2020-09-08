from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from authors.models import Author
from listings.choices import author_choice, price_choice, duration_choice

def index(request):
    listings = Listing.objects.order_by('-complete_date')[:3]
    context = {
        'listings': listings,
        'author_choice': author_choice,
        'price_choice': price_choice,
        'duration_choice': duration_choice
    }
    return render(request, 'pages/index.html', context)

def about(request):
    authors = Author.objects.order_by('id')
    context = {
        'authors': authors
    }
    return render(request, 'pages/about.html', context)
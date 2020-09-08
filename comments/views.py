from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Comment

# Create your views here.
def comment(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        # listing = request.POST['listing']
        name = request.POST['name']
        message = request.POST['message']
        # date = request.POST['date']
        user_id = request.POST['user_id']

        comment = Comment(listing_id = listing_id, title=name, message = message, user_id = user_id)
        comment.save()

        messages.success(request, 'Submitted. Thank you for your feedback.')
        return redirect('/listings/'+listing_id)
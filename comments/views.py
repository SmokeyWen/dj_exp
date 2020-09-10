from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Comment
from django.core.mail import send_mail

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

        send_mail(
            'New Comment on Painkey',
            'There is a new comment for Miniature No.' + listing_id + ' from ' + name + ' saying: ' + message,
            'painkey.com',
            ['835033838wen@gmail.com'],
            fail_silently = False
        )

        messages.success(request, 'Submitted. Thank you for your feedback.')
        return redirect('/listings/'+listing_id)
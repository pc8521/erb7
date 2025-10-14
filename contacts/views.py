from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

# Create your views here.

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        if request.user.is_authenticated:
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('listings:listing', listing_id=listing_id)
        contact = Contact(
            listing=listing,
            listing_id=listing_id,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id
        )
        contact.save()
        messages.success(request, 'Your inquiry has been submitted, a representative will get back to you soon')
        return redirect('listings:listing', listing_id=listing_id)

def delete_contact(request, contact_id):
    pass

def edit_contact(request, contact_id):
    pass

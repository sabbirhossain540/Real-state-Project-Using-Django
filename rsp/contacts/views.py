from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail

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
        realtor_email = request.POST['realtor_email']

        #Check if user has made inquery already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                print("You have already made a enquery")
                return redirect('/listings/'+listing_id)


        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()

        #Send Email
        send_mail(
            'Property Listing Inquery',
            'There has been an inquery for '+ listing + '. Sign into the admin panel for more info',
            'ashes545454@gmail.com', #Host mail
            ['job.sabbirhossain308@gmail.com'], #Where We want to sent mail
            fail_silently=False
        )



        print("Data Submitted Successfully")
        return redirect('/listings/'+listing_id)



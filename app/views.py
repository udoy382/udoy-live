from operator import le
from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        company_name = request.POST['company_name']
        phone_number = request.POST['phone_number']
        city = request.POST['city']
        message = request.POST['message']

        if len(first_name and last_name) > 20:
            messages.error(request, 'Oops! ERROR. Your name must be 5 to 20 character.')
        elif first_name == '':
            messages.error(request, 'Oops! ERROR. Name field is required.')
        elif last_name == '':
            messages.error(request, 'Oops! ERROR. Name field is required.')
        elif phone_number == '':
            messages.error(request, 'Oops! ERROR. Number field is required.')
        elif email == '':
            messages.error(request, 'Oops! ERROR. Email field is required.')
        elif message == '':
            messages.error(request, 'Oops! ERROR. Message field is required.')
        else:
            contact = Contact(first_name=first_name, last_name=last_name, email=email, company_name=company_name, phone_number=phone_number, city=city, message=message)
            contact.save()
            messages.success(request, 'Your form has been submitted successfully!')

    return render(request, 'contact.html')

def image(request):
    return render(request, 'image.html')
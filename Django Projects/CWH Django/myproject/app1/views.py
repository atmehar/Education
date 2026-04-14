from django.shortcuts import render 
#from django.http import HttpResponse
from datetime import datetime
from app1.models import contact as ContactModel
from django.contrib import messages

# Create your views here.

 
def index(request):
    messages.success(request, "this is a test messge")
    return render(request , "app1/index.html" ,)
    # return HttpResponse("Welcome to my website")

def about(request):
    return render(request , "app1/about.html" ,)

def services(request):
    return render(request , "app1/service.html" ,)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('Name') or ''
        email = request.POST.get('Email') or ''
        phone = request.POST.get('phone') or ''
        desc = request.POST.get('desc') or ''
        contact_entry = ContactModel(name=name, email=email, phone=phone,
        desc=desc, date=datetime.today())
        contact_entry.save()
        messages.success(request, "Your message has been sent.")

    return render(request , "app1/contact.html" ,)

def base(request):
    return render(request , "app1/base.html" ,)

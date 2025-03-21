from django.shortcuts import render
from .models import Services
from app.forms import Contact_Form
from django.contrib import messages
# Create your views here.


def Home_view(request):
    repeat_count = range(2)  
    return render(request,'home.html',{'repeat_count': repeat_count})


def About_us_view(request):
    return render(request,"aboutus.html")


def Condact_view(request):
    if request.method=="POST":
        form=Contact_Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        
        form=Contact_Form()
    return render(request,"contact.html",{"form":form,})


def Service_view(request):
    repeat_count = range(2)  
    service=Services.objects.all()
    return render(request,"service.html",{"services":service,'repeat_count': repeat_count})
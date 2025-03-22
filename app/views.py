from django.shortcuts import render
from .models import Services
from app.forms import Contact_Form
from django.contrib import messages
from django.core.mail import send_mail
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
            messages.success(request,"Successfully submitted the Form")
            contact=form.save()
            subject=f"New Enquiry Submitted - {contact.service}"
            message=f"""
            Service: {contact.service}
            Name:{contact.name}
            Phone:{contact.phone}
            email:{contact.email}
            Date choose{contact.choose_date}
            Message: {contact.message}            
"""
            send_mail(
                subject=subject,
                message=message,
                from_email="abhinavabhi192018@gmail.com",
                recipient_list=["abhinavabhi192018@gmail.com"],
                fail_silently=False
            )
        else:
            messages.error(request,"Form submission failed. Please try again")

    else:
        form=Contact_Form()
    return render(request,"contact.html",{"form":form,})


def Service_view(request):
    repeat_count = range(2)  
    service=Services.objects.all()
    return render(request,"service.html",{"services":service,'repeat_count': repeat_count})


def gallery(request):
    return render(request,"gallery.html")
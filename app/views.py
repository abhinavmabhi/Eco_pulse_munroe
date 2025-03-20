from django.shortcuts import render
from .models import Services
from app.forms import Contact_Form
from django.contrib import messages
# Create your views here.


def Home_view(request):
    service=Services.objects.all()
    repeat_count = range(2)  
    if request.method=="POST":
        form=Contact_Form(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(messages.error)
    else:
        
        form=Contact_Form()
    return render(request,'home.html',{"form":form,"services":service,'repeat_count': repeat_count})
from django.db import models


# Create your models here.
class Services(models.Model):

    name=models.CharField(max_length=200)
    price=models.IntegerField()
    description=models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to="service images")

class Contact(models.Model):

    choice=(
        ("Home Stay","Home Stay"),
        ("Canal Boating","Canal Boating"),
        ("kayaking","kayaking"),
        ("Shikkara","Shikkara"),
    )
    service=models.CharField(max_length=200, choices=choice, default="Home Stay")
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=12)
    message=models.TextField()
    choose_date=models.DateTimeField()
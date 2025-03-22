from app.models import Contact
from django import forms

class Contact_Form(forms.ModelForm):
    class Meta:
        model=Contact
        fields=["name","service","phone","email","message","choose_date"]

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control border border-2","placeholder":"Enter Name"}),
            "service":forms.Select(attrs={"class":"form-select border border-2"}),
            "phone":forms.TextInput(attrs={"class":"form-control border border-2","placeholder":"Enter Phone"}),
            "email":forms.EmailInput(attrs={"class":"form-control border border-2","placeholder":"Enter Email"}),
            "message": forms.Textarea(attrs={"class": "form-control border border-2", "rows": 3, "placeholder": "Enter Message..."}),
            "choose_date": forms.DateTimeInput(attrs={"class": "form-control border border-2", "type": "datetime-local"}),
        }
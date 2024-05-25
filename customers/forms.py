
from django import forms
from .models import Customer
class CustomerSignupForm(forms.ModelForm):
    class Meta:
        model =Customer
        fields =['username','email', 'phone', 'address'] 
        #include other fields here
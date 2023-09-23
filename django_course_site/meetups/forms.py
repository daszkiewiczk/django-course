from .models import Participant
from django import forms

# class RegistrationForm(forms.ModelForm):    
#     class Meta:
#         model = Participant
#         fields = ("email",)

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your email')

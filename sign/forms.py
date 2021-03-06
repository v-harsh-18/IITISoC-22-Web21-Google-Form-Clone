from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email=forms.EmailField()
    name=forms.CharField(max_length=50)

    class Meta:
        model=User
        fields=['username','email','name','password1','password2']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['password1'].help_text=None
        self.fields['password2'].help_text=None
        self.fields['username'].help_text=None

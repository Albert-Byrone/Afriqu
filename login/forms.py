from django import forms
from login.models import *
from django.contrib.auth.forms import UserCreationForm
import random
import string
from .emails import send_credentials

def randomPassword(stringLength=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput,required=False)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput,required=False)
    
    
    class Meta:
        model = User
        fields = ['groups','email','name','password','is_staff']
    def cleaned_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password does not match")
        return password2


    def save(self,commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        password = randomPassword()
        user.set_password(password)
        user.save()
        email =user.email
        send_credentials(password,email)
        return user

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['groups','email','name','password','is_staff']

    def clean_password(self):
        return self.initial["password"]



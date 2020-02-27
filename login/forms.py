from django import forms
from login.models import *
from django.contrib.auth.forms import UserCreationForm
import random
import string
from .emails import send_credentials

def randomPassword(stringLength=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['groups','email','name','password','is_staff']

class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['groups','email','name','password','is_staff']

    def cleaned_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password does not match")
        return password2


    def create_user(self,commit=True):
        user = super(UserForm, self).save(commit=False)
        print(user,"hfgfgfg")
        user.set_password(self.cleaned_data["password1"])
        credentials = self.cleaned_data["password1"]
        email = user.email
        name = user.name
        send_credentials(credentials,name,email)








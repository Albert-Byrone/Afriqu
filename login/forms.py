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
    
    print(password1, "cleaned password 1")
    print(password2,"cleaned password 2")
    
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
        print(password)
        user.set_password(password)
        user.save()
        email =user.email
        send_credentials(password,email)
        return user

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    # password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ['groups','email','name','password','is_staff']

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]



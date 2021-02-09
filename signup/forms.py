from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core import validators
import re


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, )
    last_name = forms.CharField(max_length=30, required=False, )
    email = forms.EmailField(max_length=254, help_text='Required')
    username = forms.CharField(required=True, help_text=False)
    password1 = forms.CharField(required=True, help_text=False, label='Password', widget = forms.PasswordInput())
    

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email','username', 'password1', 'password2']

    
    def clean_username(self):
        username = self.cleaned_data['username']
        reg = re.compile('[_!#$%^&*()<>?/\|}{~:]')

        if username[0].isdigit():
            raise forms.ValidationError("Username should begin with alphabets a-z or A-Z")
        elif not any(c.isdigit() for c in username):
            raise forms.ValidationError("Username should contain atleast one number")
        elif reg.search(username) == True:
            raise forms.ValidationError("Username should not contain special characters")
        elif len(username) > 15:
            raise forms.ValidationError("Username should not be more than 15 characters")
        else:
            return username

    
    def clean_password1(self, *args):
        password = self.cleaned_data['password1']
        # username = self.cleaned_data['username']
        
        if not password.isalnum():
            raise forms.ValidationError("password should contain atleast one number")
        elif len(password) > 15:
            raise forms.ValidationError("Password should not be more than 15 characters")
        elif len(password) < 8:
            raise forms.ValidationError("Password should be more than 8 characters")
        else:
            return password

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=False, )
    password = forms.CharField(required=True, help_text=False, label='Password', widget = forms.PasswordInput())
from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.core.exceptions import ValidationError
from django import forms
from . import models
from .models import RegisterModel
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True,widget=forms.TextInput(attrs={"placeholder":"First name",}),)
    last_name = forms.CharField(required=True,widget=forms.TextInput(attrs={"placeholder":"Last Name",}),)
    phone = forms.CharField(required=True,widget=forms.TextInput(attrs={"placeholder":"Phone Number",}),)
    email = forms.CharField(required=True,widget=forms.TextInput(attrs={"placeholder":"Email Address",}),)
    address = forms.CharField(required=True,widget=forms.TextInput(attrs={"placeholder":"Address",}),)
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={"placeholder":"Password",}),)

    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password",}),)

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name.isalpha():
            raise forms.ValidationError("First name should only contain letters")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not last_name.isalpha():
            raise forms.ValidationError("Last name should only contain letters")
        return last_name


    def clean_email(self):
        email = self.cleaned_data['email']
        if RegisterModel.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.Please use a different email")
        return email
    #
    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError("The two password didn't match")

        if len(password1) < 8:
            raise forms.ValidationError("Password must contain at least 8 characters")
        if password1 == '12345678':
            raise forms.ValidationError("Password is too common")

        return password1

    def clean_phone(self):
        phone_number = self.cleaned_data.get('phone')  # Use 'phone' instead of 'phone_number'
        if not phone_number.isdigit() or len(phone_number) != 10:
            raise forms.ValidationError('Invalid phone number. Please enter a 10-digit number.')
        return phone_number

    class Meta:
        model = RegisterModel
        fields = ('first_name','last_name','phone','email','address','password1','password2')

class LoginForm(forms.Form):
    email = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Email", }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={"placeholder": "Password", }))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if email and password:
            # Attempt to authenticate the user
            user = authenticate(email=email, password=password)
            if user is None:
                # Raise a form validation error for the "email" field
                self.add_error('email', "The Email or Password you entered doesn't match an account")
            return cleaned_data




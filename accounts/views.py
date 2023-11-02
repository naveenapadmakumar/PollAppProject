from django.contrib import auth, messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import ValidationError
from django import forms
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, FormView
from .forms import RegisterForm, LoginForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login
from .models import RegisterModel
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm

from django.contrib.auth import views as auth_views
from django.contrib.auth import get_user_model

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views import View
from django.http import JsonResponse
from .forms import LoginForm
from django import forms


# Create your views here.

User = get_user_model()
def home(request):
    return render(request,'home.html')


# Sign Up View
class RegisterView(SuccessMessageMixin,FormView):
    form_class = RegisterForm
    template_name = 'accounts/signup.html'
    success_message = "Successfully Registered.Please log in."

    def form_valid(self,form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        # Use reverse() to specify the URL name for the login page
        return reverse('login')


class LoginView(View):
    template_name = 'accounts/registration/login.html'

    def get(self, request):
        form = LoginForm()
        context = {
            'form1': form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(request=request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error('email', "The Email or Password you entered doesn't match an account")

        context = {
            'form1': form,
        }
        return render(request, self.template_name, context)


def logout(request):
    auth.logout(request)
    return redirect('login')

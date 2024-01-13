from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

class CustomLoginView(LoginView):
    template_name = 'login.html'

class MainView(View):
    template_name = 'main.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        return render(request, 'contact.html')

def user_login(request):
    if request.method == 'POST':
        return redirect('main')
    else:
        return CustomLoginView.as_view()(request)

def user_register(request):
    if request.method == 'POST':
        return redirect('second')  
    else:
        return render(request, 'register.html')

class LoginMainView(View):
    template_name = 'register.html' 

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class SecondView(View):
    template_name = 'second.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

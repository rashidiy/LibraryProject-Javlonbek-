from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import UserRegistrationForm
# Create your views here.
def signup_view(request):
    form = None
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            User.is_active=False
            form.save()
            return redirect(reverse_lazy('login'))
    return render(request, 'registration/signup.html', {'form': form})


def login_view(request):
    form = None
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You are now logged in')
                return redirect(reverse_lazy('home'))
            else:
                messages.error(request, 'Invalid username or password')
    return render(request, 'registration/login.html', {'form': form})


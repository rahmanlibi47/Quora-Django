from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                return redirect('homepage')
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    error_message = None  

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                error_message = 'Invalid credentials'  

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'error_message': error_message})


def user_logout(request):
    logout(request)
    return redirect('homepage')

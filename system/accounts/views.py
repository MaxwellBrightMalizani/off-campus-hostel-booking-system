from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.utils.http import url_has_allowed_host_and_scheme
from .forms import CustomUserCreationForm, EmailLoginForm


def register_view(request):
    """Handles registration for both students and hostel owners."""
    if request.user.is_authenticated:
        return redirect('listings:home')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome, {user.first_name or user.email}! Your account has been created.")
            return redirect('listings:home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    """Handles login using email and password."""
    if request.user.is_authenticated:
        return redirect('listings:home')

    if request.method == 'POST':
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            email    = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user     = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.first_name or user.email}!")
                next_url = request.GET.get('next')
                if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()}):
                    return redirect(next_url)
                return redirect('listings:home')
            else:
                messages.error(request, "Invalid email or password. Please try again.")
        else:
            messages.error(request, "Please fill in both fields.")
    else:
        form = EmailLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    """Logs the user out and redirects to the login page."""
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('accounts:login')

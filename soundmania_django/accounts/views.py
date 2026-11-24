from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from .forms import EmailLoginForm, RegistrationForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = RegistrationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Your Sound Mania account has been created.")
        return redirect("home")

    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = EmailLoginForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data["email"].strip().lower()
        password = form.cleaned_data["password"]
        user_record = User.objects.filter(email__iexact=email).first()
        user = authenticate(request, username=user_record.username, password=password) if user_record else None

        if user is not None:
            login(request, user)
            request.session.set_expiry(60 * 60 * 24 * 14 if request.POST.get("remember_me") else 0)
            return redirect("home")

        messages.error(request, "Invalid email or password. Please try again.")

    return render(request, "accounts/login.html", {"form": form})


@login_required
def home_view(request):
    return render(request, "accounts/home.html")


def logout_view(request):
    if request.method == "POST":
        logout(request)
    return redirect("login")

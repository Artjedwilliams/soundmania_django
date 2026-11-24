from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"placeholder": "Enter your first name", "autocomplete": "given-name"}),
    )
    last_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"placeholder": "Enter your last name", "autocomplete": "family-name"}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "username@example.com", "autocomplete": "email"}),
    )
    agree_terms = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        email = self.cleaned_data["email"].strip().lower()
        user.username = email
        user.email = email
        user.first_name = self.cleaned_data["first_name"].strip()
        user.last_name = self.cleaned_data["last_name"].strip()
        if commit:
            user.save()
        return user


class EmailLoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "username@example.com", "autocomplete": "email"}),
    )
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={"placeholder": "Enter your password", "autocomplete": "current-password"}),
    )

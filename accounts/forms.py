from django import forms
from accounts.models import User, Administrator, Customer
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.db import transaction
from django.forms import ModelForm


# User Creation Form in the Django Admin
class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ("username", "full_name", "phone", "email")

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation", widget=forms.PasswordInput)

    def cleaned_password(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don\'t match.")

        return password2

    def save(self, commit=False):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

        return user

    # User Change form for the django Admin Panel


class UserChangeForm(ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ("username", "full_name", "phone", "is_active", "is_admin",
                  "is_administrator", "is_dealer", "is_customer", "is_staff")

    def cleaned_password(self):
        return self.initial["password"]


class UserSignUpForm(ModelForm):
    email = forms.EmailField(max_length=156, required=True)
    phone = forms.CharField(max_length=20, required=True)

    class Meta:
        model = User
        fields = ('username', "phone", 'email')

    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password don\'t match!')

        return password2

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_active = False
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

        return user

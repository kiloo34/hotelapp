# from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}))
    password1 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control pwstrength', 'type': 'password'}))
    password2 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


class LoginUserForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User

        fields = [
            'username',
            'password'
        ]

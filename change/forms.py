from django import forms
from .models import Complaint
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('c_name', 'c_category', 'directed_to',)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)


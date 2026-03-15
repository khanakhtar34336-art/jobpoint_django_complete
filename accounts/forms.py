
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'contact',
            'about',
            'degree',
            'institute',
            'graduation_year',
            'is_employer',   # ✅ add here
            'profile_photo',
            'resume',
        ]
from collections import UserDict
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username  إسم المستخدم',
        'class': 'w-full py-4 px-6 rounded-xl',
        'aria-label': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password  كلمة المرور',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))

class SignupForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username  إسم المستخدم',
        'class': 'w-full py-4 px-6 rounded-xl',
        'aria-label': 'Username'
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email  البريد الإلكتروني',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password  كلمة المرور',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password  إعادة كلمة المرور',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))

    class Meta: 
        model = User
        fields = ('username', 'email', 'password1', 'password2')
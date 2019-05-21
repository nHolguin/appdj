from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Username'}),
    label="Username")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Your Password'}),
    label="Password")
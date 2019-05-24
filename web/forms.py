from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils import timezone
from .models import Empleado

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Username'}),
    label="Username")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Your Password'}),
    label="Password")

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'posicion', 'oficina', 'edad', 'salario']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'posicion': forms.TextInput(attrs={'class':'form-control','placeholder':'Position'}),
            'oficina': forms.TextInput(attrs={'class':'form-control','placeholder':'Office'}),
            'edad': forms.TextInput(attrs={'class':'form-control','placeholder':'Age'}),
            'salario': forms.TextInput(attrs={'class':'form-control','placeholder':'Salary'})
        }
"""
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
    position = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Position'}))
    office = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Office'}))
    age = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Age'}))
    start = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','value':timezone.now(),'disabled':True}))
    salary = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Salary'}))
    """
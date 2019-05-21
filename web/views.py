from django.shortcuts import render
from .forms import LoginForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def log_in(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'web/login.html', {'form':LoginForm})
    return render(request, 'web/login.html', {'form':LoginForm})

def log_out(request):
    logout(request)
    return redirect('log_in')

def home(request):
    if not request.user.is_authenticated:
        return render(request, 'web/login.html', {'form':LoginForm})
    else:
        return render(request, 'web/home.html')

def table(request):
    if not request.user.is_authenticated:
        return render(request, 'web/login.html', {'form':LoginForm})
    else:
        return render(request, 'web/table.html')

def charts(request):
    if not request.user.is_authenticated:
        return render(request, 'web/login.html', {'form':LoginForm})
    else:
        return render(request, 'web/charts.html')

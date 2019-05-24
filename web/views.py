from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, EmployeeForm
from .models import Empleado
from django.shortcuts import redirect
from django.utils import timezone

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
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmployeeForm()
    empleados = Empleado.objects.filter(inicio__lte=timezone.now()).order_by('nombre')
    return render(request, 'web/table.html', {'empleados':empleados,'form':EmployeeForm})

def charts(request):
    if not request.user.is_authenticated:
        return render(request, 'web/login.html', {'form':LoginForm})
    else:
        return render(request, 'web/charts.html')

def delete_employee(request, pk):
    empleado = Empleado.objects.get(id=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect('table')
    return render(request, 'web/delete_employee.html', {'form':EmployeeForm})

def edit_employee(request, pk):
    empleado = Empleado.objects.get(id=pk)
    if request.method == 'GET':
        form = EmployeeForm(instance=empleado)
    else:
        form = EmployeeForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('table')
    return render(request,'web/edit_employee.html',{'form':form})
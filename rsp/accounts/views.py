from django.shortcuts import render, redirect

# Create your views here.

def login(request):
    return render(request,'accounts/login.html')


def register(request):
    if request.method == 'POST':
        print('submited REG')
        return redirect('register')
    else:
        return render(request,'accounts/register.html')

def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request,'accounts/dashboard.html')

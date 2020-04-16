from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
#from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print("You are now Login")
            return redirect('dashboard')
        else:
            print("Invalid User name and Password")
            return redirect('login')


    else:
        return render(request,'accounts/login.html')

    


def register(request):
    if request.method == 'POST':
        #message.error(request, 'Testing error Message')

        # Get From values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #Check if Password match
        if password == password2:
            #Check User
            if User.objects.filter(username=username).exists():
                print("Username Already Taken")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    print("That email is being used")
                    return redirect('register')
                else:
                    #Look Good
                    user = User.objects.create_user(username=username, password=password, email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    print("User Save Successfully")
                    return redirect('login')
                    #Login after registration
                    #auth.login(request, user)
            
        else:
            print("Password and Password2 Can not match")
            return redirect('register')

    else:
        return render(request,'accounts/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        print("You are successfully Logged out")
        return redirect('index')


def dashboard(request):
    return render(request,'accounts/dashboard.html')

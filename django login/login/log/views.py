from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate, login

def log(request):
     if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        if not  User.objects.filter( username =username).exists():
                messages.error(request ,'Invalid username')
                return redirect('/login/')
            
        user = authenticate(username=username, password=password)
        
        if user is not None:
                messages.error(request ,'Invalid password')
                return redirect('/login/')
        else:
             login( request,user)
             return redirect('/login/')


     return render( request, 'login.html')

def reg(request):
    if request.method == "POST":

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')


        user = User.objects.create(

            first_name = first_name,
            last_name = last_name,
            )

        user.set_password(password)
        user.save()

        return redirect('/register/')

    return render (request ,'register.html')

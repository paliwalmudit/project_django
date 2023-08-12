from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
# Create your views here.

def index(request):
    card_service=Cards.objects.all()
    Data={
        'card_service':card_service,
    }
    return render(request, 'index.html',Data) 

def book(request):
    display=Cards.objects.all()
    Data={
        'display':display,
    }
        
    return render(request, 'book.html',Data) 

def appointment_form(request):
    display=Cards.objects.all()
    if request.method=='POST':
        if request.user.is_authenticated:
            username=request.user.username

        usern=username
        name=request.POST['user_name']
        email=request.POST['user_email']
        app_for=request.POST['appointment_for']
        date=request.POST['date']
        time=request.POST['time']
        
        app_form=Appointments(name=name,email=email,app_for=app_for,date=date,time=time,usern=usern)
        
        if app_form:
            app_form.save()
            return render(request,'index.html',{'message':"appointment booked return to index"})
        else:
            return render(request,'book.html',{'display':display,'n':"please recheck all fields and re-submit form"})

def register(request):
    return render(request,"register.html")

def user_signup(request):
    if request.method=='POST':
        uname=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pword=request.POST['password']
        cword=request.POST['c_password']
        
        
        if pword==cword:
            try:
                my_user=User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=email,password=pword)
                my_user.save()
            except IntegrityError:
                return render(request, "register.html", {
                    "message": "Username already taken."
                })
            login(request, my_user)
            
            return render(request,"index.html")
        
        else:
            return render(request,"register.html",{'message':"password and confirm password must match!!"})

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pword=request.POST.get('password')
     
        user=authenticate(request,username=username,password=pword)
        
        if user is not None:
            login(request,user)
            
            return render(request,"index.html")
            
        else:
            return render(request,"register.html",{'message':"Invalid Username or Password!!"})

def user_logout(request):
    logout(request)
    return render(request,"index.html")

def service(request):
    display=Cards.objects.all()
    data={"display":display}
    return render(request,"services.html",data)

def inside(request,name):
    display=Cards.objects.filter(card_name=name)
    data={'display':display,}
    return render(request, 'inside.html',data) 

def faq(request):
    return render(request,"FAQ.html")

def contactus(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        
        form=Contactus(fname=fname,lname=lname,email=email,subject=subject,message=message)
        form.save()
        return redirect('/')
    return render(request,'contactus.html')

def profile(request):
    if request.user.is_authenticated:
        usern=request.user.username
    display=Appointments.objects.filter(usern=usern)

    return render(request,'profile.html',{'display':display})
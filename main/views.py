from django.shortcuts import render
from .models import *
from django.http import HttpResponse

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
        name=request.POST['user_name']
        email=request.POST['user_email']
        app_for=request.POST['appointment_for']
        date=request.POST['date']
        time=request.POST['time']
        
        app_form=Appointments(name=name,email=email,app_for=app_for,date=date,time=time)
        
        if app_form:
            app_form.save()
            return render(request,'index.html',{'message':"appointment booked return to index"})
        else:
            return render(request,'book.html',{'display':display,'n':"please recheck all fields and re-submit form"})

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


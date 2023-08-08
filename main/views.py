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


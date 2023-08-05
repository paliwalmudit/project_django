from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    card_service=Cards.objects.all()
    Data={
        'card_service':card_service,
    }
    return render(request, 'index.html',Data) 

def inside(request,name):
    display=Cards.objects.filter(card_name=name)
    data={'display':display,}
    return render(request, 'inside.html',data) 

def parent1(request):
    return render(request, 'parent1.html')
def parent2(request):
    return render(request, 'parent2.html')
def parent3(request):
    return render(request, 'parent3.html')
def parent4(request):
    return render(request, 'parent4.html')

from . import views
from django.urls import path , include


app_name='main'

urlpatterns = [
    path('',views.index , name='index'),
    path('inside/<str:name>/',views.inside,name='inside'),
    path('book/',views.book,name='book'),
    path('service/',views.service,name='service'),
    path('faq/',views.faq,name='faq'),
      
]
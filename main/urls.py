from . import views
from django.urls import path , include


app_name='main'

urlpatterns = [
    path('',views.index , name='index'),
    path('inside/<str:name>/',views.inside,name='inside'),
    path('book/<str:name>',views.book,name='book'),
    path('service/<str:name>',views.service,name='service'),
    path('faq/<str:name>',views.faq,name='faq'),
      
]
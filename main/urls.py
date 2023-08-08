from . import views
from django.urls import path , include


app_name='main'

urlpatterns = [
    path('',views.index , name='index'),
    path('<str:name>/',views.inside,name='inside'),
    path('book/<str:name>',views.book,name='book'),
    path('parent1/',views.parent1,name='parent1'),
    path('parent2/',views.parent2,name='parent2'),
    path('parent3/',views.parent3,name='parent3'),
    path('parent4/',views.parent4,name='parent4'),
      
]
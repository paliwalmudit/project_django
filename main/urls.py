from . import views
from django.urls import path , include


app_name='main'

urlpatterns = [
    path('',views.index , name='index'),
    path('inside/<str:name>/',views.inside,name='inside'),
    path('book/',views.book,name='book'),
    path('service/',views.service,name='service'),
    path('faq/',views.faq,name='faq'),
    path('appointment_form/',views.appointment_form,name='appointment_form'),
    path('register/',views.register,name='register'),
    path('signup/',views.user_signup,name='user_signup'),
    path('login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('Contact_us/',views.contactus,name='contact'),
    path('Profile/',views.profile,name='profile'),
    path('About/',views.about,name='about'),
    path("Blogs/",views.blogs,name="blogs"),    
    path("Add_Blogs/",views.add_blog,name="add_blog"),
    path("blog_inside/<str:name>/",views.blog_inside,name="blog_inside"),
      
]
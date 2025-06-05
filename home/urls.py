from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact),
    path('booking',views.booking),
    path('department',views.department),
    path('doctor',views.doctor),
]
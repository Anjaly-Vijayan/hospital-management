from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact, name="contact"),
    path('booking',views.booking,name="booking"),
    path('department',views.department,name="department"),
    path('doctor',views.doctor, name="doctor"),
]
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def doctor(request):
    return render(request,'doctor.html')

def department(request):
    return render(request,'department.html')

def booking(request):
    return render(request,'booking.html')

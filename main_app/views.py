from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')
def login(request):
    return render(request, 'login.html')
def patients_details(request):
    return render(request, 'patients/details.html')
def patients_index(request):
    return render(request, 'patients/index.html')
def registration_signup(request):
    return render(request, 'registration/signup.html')
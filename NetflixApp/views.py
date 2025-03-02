from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'NetflixApp /index.html')

def login(request):
    return render(request, 'NetflixApp/login.html')

def signup(request):
    return render(request, 'NetflixApp/signup.html')
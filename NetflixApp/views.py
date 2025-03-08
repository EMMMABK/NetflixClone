from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.

def index(request):
    return render(request, 'NetflixApp/index.html')

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, "NetflixApp/login.html", {"form": form})

def signup(request):
    errors = []
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            errors = [error for error_list in form.errors.values() for error in error_list]

    else:
        form = UserCreationForm()
    
    return render(request, "NetflixApp/signup.html", {"form": form, "errors": errors})

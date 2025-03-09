from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

def index(request):
    return render(request, 'NetflixApp/index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials are invalid!')
            return redirect('login')
        
    return render(request, 'NetflixApp/login.html')

def user_logout(request):
    logout(request)
    return(redirect('/'))

def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                return redirect('/')
        else:
            messages.info(request, 'Password not matching')
            return redirect('signup')

    else:
        return render(request, 'NetflixApp/signup.html')

@login_required(login_url='login')
def movie(request):
    movies = Movie.objects.all()

    context = {
        'movies': movies, 
    }

    return render(request, 'NetflixApp/movie.html', context )

def movie_detail(request, uu_id):
    movie = get_object_or_404(Movie, uu_id=uu_id)
    return render(request, 'NetflixApp/movie_detail.html', {'movie': movie})
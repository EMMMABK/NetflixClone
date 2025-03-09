from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('movie/', views.movie, name='movie'),
    path('movie/<uuid:uu_id>/', views.movie_detail, name='movie_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
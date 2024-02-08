from django.urls import path
from .views import *

urlpatterns = [
    path('', mainView, name='index'),
    path('home', homeView, name='home'),
    path('login/', loginUser, name='login'),
    path('register/', registerUser, name='register')
]
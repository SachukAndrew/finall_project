from django.contrib.auth import login
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    # post views
    path('login/', views.user_login, name='login')
]
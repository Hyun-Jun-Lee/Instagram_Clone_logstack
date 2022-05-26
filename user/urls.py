from django.urls import path
from . import views

urlpatterns = [
    path('login', views.Login.as_view(), name='login'),
    path('join', views.Join.as_view(), name='join'),
]

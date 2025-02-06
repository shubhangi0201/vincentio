from django.urls import path
from Base import views  # Ensure correct case usage

urlpatterns = [
    
    
    path('Home/', views.Home, name='Home'),
    path('', views.Home, name='Base'),
      # Correct reference to views
]
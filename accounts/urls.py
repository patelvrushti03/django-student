from django.urls import path,include
from . import views
from django.contrib import admin

urlpatterns = [
    
    path('login/', views.user_login, name='login'),
    path('', include('students.urls')), 

]
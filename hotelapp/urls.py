from django.contrib import admin
from django.urls import path

from hotel import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),

    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('guest/', views.guest, name='guest'),
    path('logout/', views.logout, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('fasilitas/', views.fasilitas, name='fasilitas'),
    path('chat/', views.chat, name='chat'),
]

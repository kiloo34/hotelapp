from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.hashers import make_password
from django.utils.crypto import get_random_string
from hotel.models import *

from django.contrib.auth.models import User
from django.core.paginator import Paginator

from django.contrib import messages

from .forms import *


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(
                request, 'Akun ' + user + ' Berhasil dibuat, silakan login untuk melanjutkan', extra_tags='success')
            return redirect('login')

    konteks = {
        'title': 'register',
        'subtitle': '',
        'active': 'register',
        'form': form,
    }
    return render(request, 'registration/register.html', konteks)

def guest(request):

    rand = get_random_string(length=3)
    username = 'user'+rand

    user = User.objects.create_user(
            username = 'user'+rand,
            email = username+'@email.com',
            password = make_password('1234678')
        )
    # user = authenticate(request, username=username, password=password)
    auth_login(request, user)
    
    return redirect('chat');

def login(request):
    form = LoginUserForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            if user.is_superuser or user.is_staff:
                return redirect('/admin')
            else:
                return redirect('dashboard')
        else:
            messages.info(request, 'Username atau password salah',
                          extra_tags='danger')

    konteks = {
        'title': 'login',
        'subtitle': '',
        'active': 'login',
        'form': form,
    }
    return render(request, 'registration/login.html', konteks)


def logout(request):
    auth_logout(request)
    return redirect('index')


def index(request):
    konteks = {
        'title': 'landing',
        'subtitle': '',
        'active': 'landing',
    }
    return render(request, 'user/index.html', konteks)


@login_required
def dashboard(request):
    # tempat = Tempat.objects.all()

    # p = Paginator(tempat, 3)
    # page = request.GET.get('page')
    # objek = p.get_page(page)

    konteks = {
        'title': 'dashboard',
        'subtitle': '',
        'active': 'index',
        # 'wisata': objek,
    }
    return render(request, 'user/dashboard.html', konteks)


@login_required
def fasilitas(request):
    kategori = Kategori.objects.all()
    fasilitas = Fasilitas.objects.all()
    konteks = {
        'title': 'fasilitas',
        'subtitle': '',
        'active': 'fasilitas',
        'kategori': kategori,
        'fasilitas': fasilitas
    }
    return render(request, 'user/fasilitas.html', konteks)

@login_required
def chat(request):
    # tempat = Tempat.objects.all()
    konteks = {
        'title': 'chat',
        'subtitle': '',
        'active': 'chat',
        # 'wisata': tempat,
    }
    return render(request, 'user/chat.html', konteks)

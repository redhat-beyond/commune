from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from .models import Chore, Commune


def main_page(request):
    communes = Commune.objects.all()
    context = {'communes': communes}
    return render(request, 'commune_app/index.html', context)


def commune(request):
    chores = Chore.objects.all()
    context = {'chores': chores}
    return render(request, 'commune_app/commune.html', context)


def user_signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        user_model = get_user_model()
        user_obj = user_model.objects.create_user(email=email, name=name)
        user_obj.set_password(password)
        user_obj.save()
        user_auth = authenticate(username=email, password=password)
        login(request, user_auth)
        return redirect('Main_Page')
    else:
        return render(request, 'commune_app/signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_auth = authenticate(username=username, password=password)
        login(request, user_auth)
        return redirect('Main_Page')
    else:
        return render(request, 'commune_app/login.html')


def user_logout(request):
    logout(request)
    return redirect('Main_Page')

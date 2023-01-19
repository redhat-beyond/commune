from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from .models import Chore, Commune


def main_page(request):
    return render(request, 'commune_app/index.html')


def commune(request):
    users = get_user_model().objects.all()
    context = {'users': users}
    return render(request, 'commune_app/commune.html', context)


def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user_model = get_user_model()
        user_obj = user_model.objects.create_user(username=username, password=password,email=email)
        user_obj.set_password(password)
        user_obj.save()
        user_auth = authenticate(username=username, password=password)
        login(request, user_auth)
        return redirect('main_page')
    else:
        return render(request, 'commune_app/signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'commune_app/commune.html')
        else:
            return redirect('main_page')
    else:
        return render(request, 'commune_app/login.html')

def user_logout(request):
    logout(request)
    return redirect('main_page')

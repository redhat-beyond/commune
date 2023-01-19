from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.apps import apps

Chore = apps.get_model('commune_app', 'Chore')
Commune = apps.get_model('commune_app', 'Commune')


def main_page(request):
    return render(request, 'commune_app/index.html')


def commune(request):
    User = get_user_model()
    user = User.objects.get(id=request.user.id)
    commune_id = user.commune_id.id
    if commune_id is not None:
        active_chores = Chore.objects.filter(commune_id=commune_id, completed=False, passed=True)
        chores_to_vote_on = Chore.objects.filter(commune_id=commune_id, completed=False, passed=False)
        commune = Commune.objects.filter(id=commune_id).first()
        commune_name = commune.name
        wallet = commune.wallet
        description = commune.description
        context = {'active_chores': active_chores, 'commune_name': commune_name, 'chores_to_vote_on': chores_to_vote_on,
                   'wallet': wallet, 'description': description}
        return render(request, 'commune_app/commune.html', context)
    else:
        return redirect('main_page')


def user_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user_model = get_user_model()
        user_obj = user_model.objects.create_user(username=username, password=password, email=email)
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
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'commune_app/commune.html')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'commune_app/login.html')


def user_logout(request):
    logout(request)
    return redirect('main_page')


def create_commune(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        wallet = request.POST['wallet']
        new_commune = Commune.create_commune(name=name, description=description, wallet=wallet)
        new_commune.save()
        user_id = request.user.id
        User = get_user_model()
        user = User.objects.get(id=user_id)
        user.join_commune(new_commune.id)
        return redirect('main_page')
    else:
        return render(request, 'commune_app/create_commune.html')

from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from .models import Chore, Commune


def main_page(request):
    # communes = Commune.objects.all()
    # context = {'communes': communes}
    # return redirect('commune_app/index.html')
    return render(request, 'commune_app/index.html')


def commune(request):
    users = get_user_model().objects.all()
    context = {'users': users}
#     commune_id = request.user.commune_id
#     chores = Chore.objects.filter(commune_id=commune_id,passed=False)
#     context = {'chores': chores}
    return render(request, 'commune_app/commune.html', context)
    # active_chores = Chore.objects.filter(commune_id=commune_id,completed=False,passed=True)
    # commune = Commune.objects.filter(id=commune_id).first()
    # wallet = commune.wallet
    # description = commune.description
    # context = {'active_chores': active_chores, 'chores_to_vote_on': chores_to_vote_on, 'wallet': wallet, 'description': description}
    # context = {'active_chores': active_chores, 'chores_to_vote_on': chores_to_vote_on}


def user_signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        user_model = get_user_model()
        user_obj = user_model.objects.create_user(email=email, username=name, password=password)
        user_obj.set_password(password)
        user_obj.save()
        user_auth = authenticate(username=email, password=password)
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
            return render(request, 'commune')
        else:
            return redirect('logout')
    else:
        return render(request, 'registration/login.html')

def user_logout(request):
    logout(request)
    return redirect('main_page')

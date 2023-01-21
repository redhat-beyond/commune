from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from commune_app.models import Chore, Commune, Vote


def main_page(request):
    return render(request, 'commune_app/index.html')


def get_yes_votes_for_chore(chore_id):
    return len(Vote.objects.filter(chore_id=chore_id, approve=True))


def get_no_votes_for_chore(chore_id):
    return len(Vote.objects.filter(chore_id=chore_id, approve=False
                                   ))


def has_voted(user_id, chore_id):
    return len(Vote.objects.filter(user_id=user_id, chore_id=chore_id)) > 0


def commune(request):
    commune_id = request.user.commune_id.id
    # chores = Chore.objects.filter(commune_id=commune_id, passed=False)
    active_chores = Chore.objects.filter(commune_id=commune_id, completed=False, passed=True)
    chores_to_vote_on = Chore.objects.filter(commune_id=commune_id, completed=False, passed=False)
    chores_to_vote_on = [(chore, get_yes_votes_for_chore(chore.id), get_no_votes_for_chore(chore.id),
                          has_voted(request.user.id, chore.id), chore.id) for chore in chores_to_vote_on]
    commune = Commune.objects.filter(id=commune_id).first()
    commune_name = commune.name
    wallet = commune.wallet
    description = commune.description
    context = {
        'active_chores': active_chores,
        'commune_name': commune_name,
        'chores_to_vote_on': chores_to_vote_on,
        'wallet': wallet,
        'description': description
    }
    return render(request, 'commune_app/commune.html', context)


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


def vote(request):
    if request.method == 'POST':
        if 'yes' in request.POST.keys():
            chore_id = request.POST['yes']
            chore = Chore.get_chore(chore_id)
            Vote.create_new_vote(request.user, chore, True)
        else:
            chore_id = request.POST['no']
            chore = Chore.get_chore(chore_id)
            Vote.create_new_vote(request.user, chore, False)
        return redirect('commune')
    else:
        return redirect('commune')


def user_logout(request):
    logout(request)
    return redirect('main_page')

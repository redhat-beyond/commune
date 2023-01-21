from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.apps import apps

Chore = apps.get_model('commune_app', 'Chore')
Commune = apps.get_model('commune_app', 'Commune')
Vote = apps.get_model('commune_app', 'Vote')


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


def chore(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        date = request.POST['date']
        assign_to = request.POST['assign_to']
        budget = request.POST['budget']
        commune_id = request.POST['commune_id']
        new_chore = Chore.create_chore(title=title, description=description, date=date, assign_to=assign_to,
                                       budget=budget, commune_id=commune_id)
        new_chore.save()
        return redirect('commune')
    return render(request, 'commune_app/chore.html')


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
            return render(request, 'commune_app/index.html')
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


def do_chore(request):
    if request.method == 'POST':
        chore_id = request.POST['chore_id']
        chore = Chore.get_chore(chore_id)
        chore.execute_chore(chore_id=chore_id, user_id=request.user.id)
        return redirect('commune')
    else:
        return redirect('commune')

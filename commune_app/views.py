from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from .models import Chore, Commune
from django.http import HttpResponse
from .models import Poll


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
        email = request.POST['email']
        password = request.POST['password']
        user_auth = authenticate(username=email, password=password)
        login(request, user_auth)
        return redirect('Main_Page')
    else:
        return render(request, 'commune_app/login.html')


def user_logout(request):
    logout(request)
    return redirect('Main_Page')


def votes_main(request):
    polls = Poll.objects.all()
    context = {
        'polls': polls
    }
    return render(request, 'voting/votes.html', context)


def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    # LoggedInUser = (not implemented yet)

    if request.method == 'POST':
        # if(Vote.objects.getall(user=LoggedInUser, chore=poll.chore))
        #   the user has already voted on this chore. can't vote more than once.
        #   return a fitting error message

        selected_option = request.POST['poll']

        if selected_option == 'option1':
            poll.option_one_count += 1
            # Vote(LoggedInUser, poll.chore, poll, True)
        elif selected_option == 'option2':
            poll.option_two_count += 1
            # Vote(LoggedInUser, poll.chore, poll, False)
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('results', poll.id)

    context = {
        'poll': poll
    }
    return render(request, 'voting/vote.html', context)


def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll': poll
    }
    return render(request, 'voting/results.html', context)

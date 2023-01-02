from django.shortcuts import render
from .models import Chore


def main_page(request):
    return render(request, 'commune_app/index.html')


def chores(request):
    chores = Chore.objects.all()
    context = {'chores': chores}
    return render(request, 'commune_app/chores.html', context)

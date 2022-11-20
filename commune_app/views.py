from django.shortcuts import render


def main_page(request):
    return render(request, 'commune_app/index.html')

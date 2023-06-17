from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    name = 'Edigleison'
    return render(request, 'recipes/pages/home.html', {'name': 9})

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {}
    return render(request, 'main/home.html', context)

def chores(request):
    context = {}
    return render(request, 'main/chores.html', context)

def meals(request):
    context = {}
    return render(request, 'main/meals.html', context)

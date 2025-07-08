from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def streaks(request):
    return HttpResponse("<h1> this is the streaks of the coder ")
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def problems(request):
    return HttpResponse("<h1> this is the probelm page")
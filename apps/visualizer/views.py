from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def visualizer(request):
    return HttpResponse("<h1>this is the viusalizer of the code")

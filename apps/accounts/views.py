from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def accounts(request):
    return HttpResponse("<h1>this is account section")
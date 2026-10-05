from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#function based
def home(request):

    return HttpResponse("Welcome to Django")

def index(request):
    return HttpResponse("Index page")
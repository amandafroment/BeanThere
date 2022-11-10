from django.shortcuts import render, redirect
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

# Create your views here.
def landing(request):
    return HttpResponse('<h1>Landing Page</h1>')
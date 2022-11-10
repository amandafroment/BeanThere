from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def landing(request):
    return HttpResponse('<h1>Landing Page</h1>')

# Define the home view
def home(request):
  return HttpResponse('<h1>Home</h1>')

# Define the home view
def index(request):
  return HttpResponse('<h1>Index</h1>')

# Define the details view
def details(request):
  return HttpResponse('<h1>Details</h1>')

# Define the user view
def user(request):
  return HttpResponse('<h1>Users</h1>')

# Define the review view
def review(request):
  return HttpResponse('<h1>Reviews</h1>')
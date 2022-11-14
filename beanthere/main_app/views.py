from django.shortcuts import render, redirect
from django.contrib.auth import login

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def signup (request):
  return render(request, 'signup.html')

# Define the home view
def home(request):
  return render(request, 'users/home.html')

# Define the home view
def index(request):
  return render(request, 'users/index.html')

# Define the details view
def details(request):
  return render(request, 'users/details.html')

# Define the user view
def user(request):
  return render(request, 'users/user.html')

# Define the review view
def review(request):
  return render(request, 'users/review.html')
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def landing(request):
    return render(request, 'landing.html')

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
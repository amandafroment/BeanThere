from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Review
import os
import argparse
import json
import pprint
import requests
import sys
import urllib
import datetime

from urllib.error import HTTPError
from urllib.parse import quote
from urllib.parse import urlencode
from urllib.parse import urljoin

API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
DETAILS_PATH = 'https://api.yelp.com/v3/businesses/'

API_KEY = os.environ['YELP_KEY'] 

DEFAULT_TERM = 'coffee'
DEFAULT_LOCATION = 'Toronto'
SEARCH_LIMIT = 10

DAY_NAMES = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}

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

def search(request):
  city = request.GET.get('search') #put form name here 
  response_data = api_search(API_KEY, DEFAULT_TERM, city)
  search_data = response_data.get('businesses')
  return render(request, 'users/index.html', { 'businesses': search_data })

def landing(request):
    return render(request, 'landing.html')

# Define the home view
def home(request):
  return render(request, 'users/home.html')

# Define the home view
def index(request):
  response_data = api_search(API_KEY, DEFAULT_TERM, DEFAULT_LOCATION)
  search_data = response_data.get('businesses')
  return render(request, 'users/index.html', { 'businesses': search_data })

# Define the details view
def details(request, yelp_id):
  response_data = api_details(API_HOST, DETAILS_PATH, API_KEY, yelp_id)
  hours_raw = response_data.get('hours')[0].get('open')
  hours_data = hours_format(hours_raw)
  return render(request, 'users/details.html', {'data': response_data, 'hours_data': hours_data})

def hours_format(hours_raw):
  hours_clean = []
  for day in hours_raw:
    day_info = {
      'start': format_time(day.get('start')),
      'end': format_time(day.get('end')),
      'day_name': DAY_NAMES.get(day.get('day'))
    }
    hours_clean.append(day_info)
  return hours_clean

def format_time(time):
  timeInt = int(time)
  hours = int(timeInt/100)
  minutes = timeInt - hours*100
  if minutes == 0:
    minutes = '00'
  if hours <= 12:
    return f'{hours}:{minutes} AM'
  else:
    return f'{hours-12}:{minutes} PM'

# Define the user profile view
def user(request):
  return render(request, 'users/user.html')

def create_review(request, yelp_id):
  return render(request, 'users/review.html', {'yelp_id': yelp_id})

def add_review(request, yelp_id):
  data = request.POST
  print(data)
  lighting = data['lighting']
  sound = data['sound']
  traffic = data['traffic']
  vegan = bool(data['vegan'])
  gluten_free = bool(data['gluten_free'])
  lactose_free = bool(data['lactose_free'])
  service = data['service']
  wifi = bool(data['wifi'])
  outlets = bool(data['outlets'])
  patio = bool(data['patio'])
  pet_friendly = bool(data['pet_friendly'])
  comments = data['comment-box']
  cafe_id = yelp_id
  timestamp = datetime.datetime.now()
  user = request.user
  r = Review(lighting=lighting, sound=sound, traffic=traffic, vegan=vegan, gluten_free=gluten_free, lactose_free=lactose_free, service=service, wifi=wifi, outlets=outlets, 
  patio=patio, pet_friendly=pet_friendly, comments=comments, cafe_id=cafe_id, timestamp=timestamp, user=user)
  r.save()
  return redirect('details', yelp_id=yelp_id)

def api_search(api_key, term, location):
    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }
    return api_request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)

def api_request(host, path, api_key, url_params=None):
  url_params = url_params or {}
  url = '{0}{1}'.format(host, quote(path.encode('utf8')))
  headers = {
    'Authorization': 'Bearer %s' % api_key,
  }

  print(u'Querying {0} ...'.format(url))

  response = requests.request('GET', url, headers=headers, params=url_params)

  return response.json()

def api_details(host, path, api_key, yelp_id):
  url = urljoin(path, yelp_id)
  print(url)
  headers = {
    'Authorization': 'Bearer %s' % api_key,
  }
  print(u'Querying {0} ...'.format(url))
  response = requests.request('GET', url, headers=headers)
  return response.json()


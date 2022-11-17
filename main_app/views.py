import argparse
import datetime
import json
import os
import pprint
import sys
import urllib
import requests
from urllib.error import HTTPError
from urllib.parse import quote, urlencode, urljoin
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Review, Favourite

API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
DETAILS_PATH = 'https://api.yelp.com/v3/businesses/'

API_KEY = os.environ['YELP_KEY'] 

DEFAULT_TERM = 'coffee'
DEFAULT_LOCATION = 'Toronto'
SEARCH_LIMIT = 10

DAY_NAMES = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}

NEW_REVIEW = False

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = ['Invalid sign up - try again',
        'Password must contain 8 or more characters',
        'Password must conatin letters and numbers']
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  print(error_message)
  return render(request, 'registration/signup.html', context)

@login_required
def search(request):
  city = request.GET.get('search') #put form name here 
  response_data = api_search(API_KEY, DEFAULT_TERM, city)
  search_data = response_data.get('businesses')
  return render(request, 'users/index.html', { 'businesses': search_data })

def landing(request):
    return render(request, 'landing.html')

@login_required
def home(request):
  all_reviews = Review.objects.filter(user__exact=request.user)
  selected_reviews = all_reviews.order_by('-timestamp')[:3]
  faves = Favourite.objects.filter(user__exact=request.user)
  return render(request, 'users/home.html', {'recents': selected_reviews, 'faves': faves})

@login_required
def index(request):
  response_data = api_search(API_KEY, DEFAULT_TERM, DEFAULT_LOCATION)
  search_data = response_data.get('businesses')
  return render(request, 'users/index.html', { 'businesses': search_data })

@login_required
def details(request, yelp_id):
  reviews = Review.objects.filter(cafe_id__exact=yelp_id)
  print(reviews[0].user)
  response_data = api_details(API_HOST, DETAILS_PATH, API_KEY, yelp_id)
  if response_data.get('hours'):
    hours_raw = response_data.get('hours')[0].get('open')
    hours_data = hours_format(hours_raw)
  else:
    hours_data = []
  global NEW_REVIEW
  display_overlay = NEW_REVIEW
  NEW_REVIEW = False
  if Favourite.objects.filter(cafe_id__exact=yelp_id).filter(user_id__exact=request.user).count() > 0:
    fave = True
  else:
    fave = False
  return render(request, 'users/details.html', {'data': response_data, 'hours_data': hours_data, 'reviews': reviews, 'display_overlay': display_overlay, 'fave':fave})

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

def user(request):
  return render(request, 'users/user.html')

@login_required
def create_review(request, yelp_id):
  data = request.POST
  name = data['name']
  rating = data['rating']
  price = data['price']
  images = data['image_url']
  images_strip = images.strip("[']")
  images_split = images_strip.split("', '")
  image_url = images_split[0]
  yelp_data = {
    'name': name,
    'rating': rating,
    'price': price,
    'image_url': image_url
  }
  return render(request, 'users/review.html', {'yelp_id': yelp_id, 'yelp_data': yelp_data})

def boolean_translate(bool_value):
  if bool_value == 'true':
    return True
  else:
    return False

@login_required
def add_review(request, yelp_id):
  data = request.POST
  lighting = data['lighting']
  sound = data['sound']
  traffic = data['traffic']
  vegan = boolean_translate(data['vegan'])
  gluten_free = boolean_translate(data['gluten_free'])
  lactose_free = boolean_translate(data['lactose_free'])
  service = data['service']
  wifi = boolean_translate(data['wifi'])
  outlets = boolean_translate(data['outlets'])
  patio = boolean_translate(data['patio'])
  pet_friendly = boolean_translate(data['pet_friendly'])
  comments = data['comment-box']
  cafe_id = yelp_id
  timestamp = datetime.datetime.now()
  user = request.user
  name = data['name']
  rating = data['rating']
  price = data['price']
  image_url = data['image_url']
  r = Review(lighting=lighting, sound=sound, traffic=traffic, vegan=vegan, gluten_free=gluten_free, lactose_free=lactose_free, service=service, wifi=wifi, outlets=outlets, 
  patio=patio, pet_friendly=pet_friendly, comments=comments, cafe_id=cafe_id, timestamp=timestamp, user=user, name=name, rating=rating, price=price, image_url=image_url)
  r.save()
  global NEW_REVIEW
  NEW_REVIEW = True
  return redirect('details', yelp_id=yelp_id)

def delete_review(request, review_id, yelp_id):
  return render(request, 'users/review_confirm_delete.html', {'yelp_id':yelp_id, 'review_id':review_id})

def review_confirm_delete(request, yelp_id, review_id):
  delete=Review.objects.get(id=review_id)
  delete.delete()
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
  response = requests.request('GET', url, headers=headers, params=url_params)
  return response.json()

def api_details(host, path, api_key, yelp_id):
  url = urljoin(path, yelp_id)
  headers = {
    'Authorization': 'Bearer %s' % api_key,
  }
  response = requests.request('GET', url, headers=headers)
  return response.json()

def add_favourite(request, yelp_id):
  data = request.POST
  name = data['name']
  rating = data['rating']
  price = data['price']
  images = data['image_url']
  images_strip = images.strip("[']")
  images_split = images_strip.split("', '")
  image_url = images_split[0]
  user = request.user
  timestamp = datetime.datetime.now()
  f = Favourite(name=name, rating=rating, price=price, user=user, cafe_id=yelp_id, timestamp=timestamp, image_url=image_url)
  f.save()
  return redirect('details', yelp_id=yelp_id)

def remove_favourite(request, yelp_id):
  delete = Favourite.objects.get(cafe_id=yelp_id, user=request.user)
  delete.delete()
  return redirect('details', yelp_id=yelp_id)
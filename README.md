
<img src="beanthere/main_app/static/css/images/logo.png" width="200">         

# Bean There

Bean There is an online directory for discovering your local cafe scene!
The application is catered to students and those who work from home who are looking for a change of scenery while they work.  

After signing up and logging in, you are able to find cafes in your area using the search bar!  By clicking on the cafe of your choice, you will have access to more cafe information as well as reviews left by other students and WFH'ers. 


## Authors

- [@amandafroment](https://github.com/amandafroment)
- [@matthewTiberio](https://github.com/matthewTiberio)
- [@raeganmb](https://github.com/raeganmb)
- [@rasl76](https://github.com/rasl76)


## Tech Stack

**Client:** HTML, CSS, JavaScript, Python

**Server:** Django, Postgresql

**Deployed with:** Heroku


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Example Code

views.py - defining the details view:

```views.py
from .models import Review

import requests
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
DETAILS_PATH = 'https://api.yelp.com/v3/businesses/'

API_KEY = os.environ['YELP_KEY'] 

DEFAULT_TERM = 'coffee'
DEFAULT_LOCATION = 'Toronto'
SEARCH_LIMIT = 10

DAY_NAMES = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}

NEW_REVIEW = False

# Define the details view
@login_required
def details(request, yelp_id):
  reviews = Review.objects.filter(cafe_id__exact=yelp_id)
  response_data = api_details(API_HOST, DETAILS_PATH, API_KEY, yelp_id)
  if response_data.get('hours'):
    hours_raw = response_data.get('hours')[0].get('open')
    hours_data = hours_format(hours_raw)
  else:
    hours_data = []
  global NEW_REVIEW
  display_overlay = NEW_REVIEW
  NEW_REVIEW = False
  return render(request, 'users/details.html', {'data': response_data, 'hours_data': hours_data, 'reviews': reviews, 'display_overlay': display_overlay})
```
## Demo

Insert gif or link to demo


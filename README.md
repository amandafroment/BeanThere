
<img src="main_app/static/css/images/logo.png" width="200">         

# Bean There

Available for both broswer and mobile enjoyment, "Bean There" is an online directory used for discovering your local cafe scene!  It is specifically catered to students or those who work from home and are looking for great workspaces (and caffeine) in their area.

After signing up and logging in, you are able to find cafes in your area by using the search bar!  After clicking on the cafe of your choice, you will have access to more cafe details as well as reviews left by other students and WFH'ers. You can even create a review of your own to help others decide if that workspace fits their needs.  Is there reliable wifi and lots of outlets?  Can you bring your fury friend or sit out on the patio?  Do they cater to any dietary restrictions?  Let your friends on Bean There know!



## Try it out!

![Click Here!](https://beanthereapp.herokuapp.com/)



## Authors

- [@amandafroment](https://github.com/amandafroment)
- [@matthewTiberio](https://github.com/matthewTiberio)
- [@raeganmb](https://github.com/raeganmb)
- [@rasl76](https://github.com/rasl76)

UXDI: Bijou Siu, Jessica Lee



## Tech Stack

**Client:** HTML, CSS, JavaScript, Python

**Server:** Django, Postgresql

**Deployed with:** Heroku



## Skills Used

Model creation, database creation and manipulation, CRUD operations, one-to-one/one-to-many/many-to-many, making and running migrations, object-relational-mapper, use of database API, Django built-in administrator, Django authentication, Django Template Language, url patterns, form creation, 


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



## Icebox Items and Next Steps

- AAU, I want to upload photos with my review
- AAU, I want to see my profile page
- AAU, I want to have a "forget my password" option (for developer purposes, we would have to create a User Model instead of relying on Django's built-in authorization 



## Project Link

![Click Here!](https://beanthereapp.herokuapp.com/)



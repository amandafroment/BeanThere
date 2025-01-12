<p align="center">
<img src="main_app/static/css/images/logo.png" width="300">         
</p>

# Bean There

Available for both broswer and mobile enjoyment, "Bean There" is an online directory used for discovering your local cafe scene!  It is specifically catered to students or those who work from home and are looking for great workspaces (and caffeine!) in their area.

Once you have signed up and logged in, you will be able to find cafes in your area by using the search bar thanks to the YELP Fusion API.  After clicking on the cafe of your choice, you will have access to more cafe details as well as reviews left by other students and WFH'ers. You can even create a review of your own to help others decide if that workspace fits their needs.  Is there reliable wifi and lots of outlets?  Can you bring your fury friend or sit out on the patio?  Do they cater to any dietary restrictions?  Let your friends on Bean There know!



## Try it out!

[Click Here!](https://beanthereapp.herokuapp.com/)



## Authors

- [@amandafroment](https://github.com/amandafroment)
- [@matthewTiberio](https://github.com/matthewTiberio)
- [@raeganmb](https://github.com/raeganmb)
- [@rasl76](https://github.com/rasl76)

UXDI Team: Bijou Siu, Jessica Lee



## Tech Stack

**Client:** HTML, CSS, JavaScript, Python

**Server:** Django, Postgresql

**Deployed with:** Heroku



## Skills Used

Model creation, database creation and manipulation, CRUD operations, one-to-one/one-to-many/many-to-many, making and running migrations, object-relational-mapper, use of database API, Django built-in administrator, Django authentication, Django Template Language, url patterns, form creation, error message returns, Heroku deployment, mobile-first design, media queries, overlay, -webkit- and -moz-


## Screenshots

Welcome to Bean There!:

<img src="main_app/static/css/images/readme/13.jpeg" width="1000">

Login and Sign up pages:

<img src="main_app/static/css/images/readme/12.jpeg" width="500"> <img src="main_app/static/css/images/readme/11.jpeg" width="500">

Profile Page with User's Recent Reviews and Favourite Cafes:

<img src="main_app/static/css/images/readme/4.jpeg" width="1000">

Search Results and Cafes in your area:

<img src="main_app/static/css/images/readme/8.jpeg" width="500"> <img src="main_app/static/css/images/readme/9.jpeg" width="500">

Create a Review or Delete a Review:

<img src="main_app/static/css/images/readme/10.jpeg" width="500">  <img src="main_app/static/css/images/readme/5.jpeg" width="500">

Your Review!:

<img src="main_app/static/css/images/readme/6.jpeg" width="1000">

Examples of Mobile View:

<img src="main_app/static/css/images/readme/3.jpeg" width="333"> <img src="main_app/static/css/images/readme/2.jpeg" width="333"> <img src="main_app/static/css/images/readme/1.jpeg" width="333">

## Example Code

Example taken from views.py - defining the details view:

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

Coming soon!! 

[Application Demo Video]()



## Future Enhancements (Icebox Items)

- AAU, I want to upload and post photos with my review
- AAU, I want to see my profile page, edit my user details, and add a profile photo or avatar 
- AAU, I want to have a "forget my password" option (for developer purposes, we would have to create a User Model instead of relying on Django's built-in authorization)
- AAU, I want to login through my existing account on a third-party site (OAuth)
- AAU, I want to be able to view friends' profiles and see their favourite cafes and recent reviews



## Project Link

[Click Here!](https://beanthereapp.herokuapp.com/)


## Others Links

[Trello Board](https://trello.com/b/7j1osg7L/django-group-project)

[Entity Relationship Diagram (ERD)](https://lucid.app/lucidchart/7e15e4df-87b7-4077-b626-0ce4316a2f2b/edit?viewport_l[…]C938%2C0_0&invitationId=inv_bacb5ce4-3f20-41e8-ae29-45f23a26cf32)

<img src="main_app/static/css/images/readme/D07A24D1-DC89-4F2B-9F2B-AF9FBD94BEB5.jpeg" width="500">




from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'), # Login screen
    path('signup/', views.signup, name='signup'), # Sign Up Screen
    path('home/', views.home, name='home'), # Initial search page
    path('index/', views.index, name='index'), # Search Results
    path('details/', views.details, name='details'), # Individual Cafe Details
    path('user/', views.user, name='user'), # User Profile
    path('review/', views.review, name='review'), # Review Form
    path('accounts/signup/', views.signup, name='signup'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'), # Login screen
    path('signup/', views.signup, name='signup'), # Sign Up Screen
    path('home/', views.home, name='home'), # Initial search page
    path('index/', views.index, name='index'), # Search Results
    path('details/<str:yelp_id>', views.details, name='details'), # Individual Cafe Details
    path('details/<str:yelp_id>/review/', views.create_review, name='create_review'), # Individual Cafe Details
    path('details/<str:yelp_id>/addreview/', views.add_review, name='add_review'), # Individual Cafe Details
    path('details/<str:yelp_id>/deletereview/<int:review_id>', views.delete_review, name='delete_review'), # Individual Cafe Details
    path('details/<str:yelp_id>/confirmdelete/<int:review_id>', views.review_confirm_delete, name='confirm_delete'),
    path('user/', views.user, name='user'), # User Profile
    path('accounts/signup/', views.signup, name='signup'),
    path('search', views.search, name='search'),
]

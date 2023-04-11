from django.urls import path
from .views import *

app_name = 'flix'

urlpatterns = [
    path('',Home.as_view(), name='Home'),
    path('profiles',ProfileList.as_view(), name='profile_list'),
    path('profiles/create/',ProfileCreate.as_view(), name='profile_create'),
    path('watch/<str:profile_id>/',MovieList.as_view(), name='movie_list'),
    path('watch/details/<str:movie_id>/',MovieDetails.as_view(), name='movie_details'),
    path('watch/play/<str:movie_id>/',PlayMovie.as_view(), name='movie-play'),
    
]

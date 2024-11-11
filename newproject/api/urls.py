from django.urls import path
from newapp.views import *

urlpatterns = [
    # path('index', index, name="index"),
    path('person/', persons, name='person'),
    path('classperson/', ClassPerson.as_view() , name='classperson')
]
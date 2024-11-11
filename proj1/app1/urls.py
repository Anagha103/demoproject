from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('veg/', vegg, name="vegetables"),
    path('fruits/', fruits, name="fruits"),
    path('grocery/', grocery, name="grocery"),
    path('bkng/', bookingss, name="booking"),
]
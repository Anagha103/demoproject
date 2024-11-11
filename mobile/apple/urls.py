from django.urls import path, include
from .views import *

urlpatterns = [
    path('apple/',apple, name='apple')
]
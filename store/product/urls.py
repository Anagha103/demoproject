# from django.urls import path, include
# from .views import *

# urlpatterns = [
#     path('', index, name='index'),
#     path('about/', about, name='about'),
#     path('con/',contact , name='contact1'),
#     path('self/',self, name='self'),
#     path('contact1/',contact1, name='contact1'),
#     path('basic/',basic, name='context'),
#     path('base/',base, name='base'),
#     path('home/',home, name='home'),
#     path('con2/',contact2, name='contact2'),
# ]


from django.urls import path

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('cont', cont, name="contact"),
]
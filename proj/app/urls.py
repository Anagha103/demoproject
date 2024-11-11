from django.urls import path
from .views import *

urlpatterns = [
    # path('', home, name="home"),
    path('', register_view, name="register"),
    path('/home', home, name="home"),
    # path('about/', about, name="about"),
    # path('cont/',create_cnt,name="contact"),
    # path('booking/', create_todo, name="booking"),
    # path('bkng/', bookingss, name="booking"),
    # path('dept/', deptt, name="department"),
    # path('drs/', doctor, name="doctors"),
    # path('cbvhome/', TaskListviews.as_view(), name="department"),
    # path('cbvdetail/<int:pk>', TaskDetailtview.as_view(), name="cbdetail"),
    # path('cbvupdate/<int:pk>', TaskUpdateView.as_view(), name="cbvupdate"),
    # path('cbvdelete/<int:pk>', TaskDeleteView.as_view(), name="cbvdelete"),
    # path('create/', EmployeeCreate.as_view(), name="EmployeeCreate")
    
]
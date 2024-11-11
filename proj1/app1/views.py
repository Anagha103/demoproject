from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    return render(request,'home.html')

# def vegetables(request):
#     return render(request,'vegetables.html')

def fruits(request):
    return render(request,'fruits.html')

def grocery(request):
    return render(request,'grocery.html')

# def booking(request):
#     return render(request,'booking.html')


from .forms import BookingForm

def bookingss(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    form = BookingForm()
    dict_form = {
        'form':form
    }
    return render(request, 'booking.html', dict_form)


def vegg(request):
    dict_docs = {
        'veg': Vegetables.objects.all()     
    }
    return render(request, 'vegetables.html', dict_docs)
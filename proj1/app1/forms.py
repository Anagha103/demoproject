from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        labels = {
            'f_name' : "Fruits Name: ",
            'f_price' : "Fruits Price:",
        }
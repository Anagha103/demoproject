from django.db import models

# Create your models here.

class Booking(models.Model):
    f_name = models.CharField(max_length=255)
    f_price = models.IntegerField(default=1)

    def __str__(self):
         return self.doc_name
    


class Vegetables(models.Model):
     veg_name = models.CharField(max_length=200)
     veg_price = models.IntegerField()
     veg_image = models.ImageField(upload_to='vegetables', default='default_image.jpg')

    #  def __str__(self):
        #   return self.veg_name + ' - ('+ self.veg_price + ')'
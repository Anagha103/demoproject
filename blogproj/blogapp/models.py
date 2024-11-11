from django.db import models

# Create your models here.

class Post(models.Model):
    
    title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        unique=True,
    )
        
    content = models.TextField()


    publication_date = models.DateTimeField(
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        auto_now=True,
    )


    author = models.TextField()

    def __str__(self):
         return self.title



    

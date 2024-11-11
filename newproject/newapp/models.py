from django.db import models

# Create your models here.

# class person(models.Model):
#     name = models.CharField(max_length=20)
#     age = models.IntegerField()
#     location = models.CharField(max_length=100)



class Team(models.Model):
    team_name = models.CharField(max_length=20)

    def __str__(self):
        return self.team_name
    
class person(models.Model):
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
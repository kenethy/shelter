from django.db import models

# Create your models here.
class Unburden(models.Model):
    date_now = models.DateTimeField(auto_now_add=True)
    date_unburden = models.DateTimeField()
    description = models.TextField(max_length=1000, blank=True)
    status = models.BooleanField(blank=True)
    follow = models.IntegerField(blank=True)  # variar entre 0 e 5

class User(models.Model):
    name = models.CharField(max_length=100)
    office = models.CharField(max_length=20)
    email = models.EmailField()





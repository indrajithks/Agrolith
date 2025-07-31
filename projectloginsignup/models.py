from django.db import models
from django.contrib.auth.models import User

class Vegetable(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='vegetables/')
    price = models.DecimalField(max_digits=6,decimal_places=2)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15,blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

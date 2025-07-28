from django.db import models

class Vegetable(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='vegetables/')
    price = models.DecimalField(max_digits=6,decimal_places=2)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

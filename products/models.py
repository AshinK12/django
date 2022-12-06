from django.db import models

# Create your models here.
class Product(models.Model):
    Name=models.CharField(max_length=255)
    Price=models.FloatField()
    Stock=models.IntegerField()
    Image=models.CharField(max_length=2500)    
    
class Offer(models.Model):
    code=models.CharField(max_length=19)
    description=models.CharField(max_length=20)
    discount=models.FloatField()
    
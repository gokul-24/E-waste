from django.db import models

# Create your models here.
class PickUp(models.Model):
    Username=models.CharField(max_length=64)
    Name= models.CharField(max_length=64)
    Phone= models.IntegerField()
    Pin= models.IntegerField()
    Address= models.CharField(max_length=100)
    Description= models.CharField(max_length=100)
    Buyer=models.CharField(max_length=100)

class Buy(models.Model):
    name=models.CharField(max_length=64)
    img= models.ImageField(upload_to='pics')
    desc= models.TextField()
    price= models.IntegerField()
    seller= models.CharField(max_length=100)

class ConfirmPickUp(models.Model):
    Name= models.CharField(max_length=64)
    Phone= models.IntegerField()
    Pin= models.IntegerField()
    Address= models.CharField(max_length=100)
    Description= models.CharField(max_length=100)
    Buyer=models.CharField(max_length=100)

class Cart(models.Model):
    name=models.CharField(max_length=64)
    img= models.CharField(max_length=255)
    desc= models.TextField()
    price= models.IntegerField()
    seller= models.CharField(max_length=100)
    buyer=models.CharField(max_length=100)

class order(models.Model):
    name=models.CharField(max_length=64)
    img= models.CharField(max_length=255)
    desc= models.TextField()
    price= models.IntegerField()
    seller= models.CharField(max_length=100)
    buyer=models.CharField(max_length=100)
    number=models.IntegerField()
    
class number(models.Model):
    username=models.CharField(max_length=100)
    phone=models.IntegerField()
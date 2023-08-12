from django.db import models

# Create your models here.

class Cards(models.Model):
    card_name=models.CharField(max_length=50)
    card_image=models.ImageField()
    card_heading=models.CharField(max_length=200,default=None)
    card_details=models.CharField(max_length=250,default=None)
    card_description=models.TextField()
    
    def __str__(self):
        return self.card_name
    
class Appointments(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    app_for=models.CharField(max_length=50)
    date=models.DateField()
    time=models.TimeField()
    
    def __str__(self):
        return self.name
    
class Contactus(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    subject=models.CharField(max_length=254)
    message=models.TextField()
    
    def __str__(self):
        return self.fname
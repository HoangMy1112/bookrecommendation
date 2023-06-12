from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 100) 
    description = models.CharField(max_length=100)
    price = models.FloatField()
    file = models.FileField(upload_to='uploads') #upload folder will automatic create

    def __str__(self): #method to display name of product inside db
        return self.name
    

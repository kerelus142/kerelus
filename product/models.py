from unicodedata import name
from django.db import models

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=150)
    descreption=models.TextField()
    def __str__(self):
        return self.name

class product(models.Model):
    name=models.CharField(max_length=150)
    descreption=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField()
    
    category_id=models.ForeignKey(category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class cart(models.Model):
    num=models.DecimalField(max_digits=10,decimal_places=0)
  
    pri=models.DecimalField(max_digits=10,decimal_places=0)
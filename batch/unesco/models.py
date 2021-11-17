from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Iso(models.Model):
    name = models.CharField(max_length=128)
    region = models.ForeignKey(Region,on_delete=CASCADE)
    
    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=128,null=False)
    description = models.CharField(max_length=512,null=True,blank=True)
    justification = models.CharField(max_length=512,null=True,blank=True)
    year = models.IntegerField(default=0,null=True,blank=True)
    longitude = models.FloatField(null=True,blank=True)
    latitude = models.FloatField(null=True,blank=True)
    area_hectares = models.FloatField(null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=CASCADE,null=True)
    state = models.ForeignKey(State,on_delete=CASCADE,null=True)
    iso = models.ForeignKey(Iso,on_delete=CASCADE,null=True)
    # region = models.ForeignKey(Region,on_delete=CASCADE)

    def __str__(self):
        return self.name
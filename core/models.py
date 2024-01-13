from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 60)
    roll = models.IntegerField()
    city = models.CharField(max_length = 100)
    

class Resource(models.Model):
    name = models.CharField(max_length = 60)
    brand = models.CharField(max_length = 200)
    storage = models.CharField(max_length = 10)
    mother_board = models.CharField(max_length = 200)
    memory = models.CharField(max_length = 10)
    budget_year = models.IntegerField()
    others = models.CharField(max_length = 200)


from django.db import models

# Create your models here.

class Drink(models.Model):
    name = models.CharField(max_length=100)
    litre = models.IntegerField()

    def __str__(self):
        return self.name

class Sweet(models.Model):
    name = models.CharField(max_length=100)
    mass = models.IntegerField()

    def __str__(self):
        return self.name

from django.db import models

class Dealer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.make} {self.model} - {self.year}"

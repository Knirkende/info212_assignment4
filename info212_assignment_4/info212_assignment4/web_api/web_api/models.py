from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=50)

    def __str__(self): 
        return self.make + ' ' + self.carmodel

class Customer(models.Model):
    booked_car = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)

    def __str__(self): 
        return self.name + ' ' + self.booked_car

class Employee(models.Model):
    empname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    adress = models.CharField(max_length=50)

    def __str__(self): 
        return self.name + ' ' + self.empname
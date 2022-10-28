from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=50)

    def __str__(self): 
        return self.make + ' ' + self.carmodel

class Customer(models.Model):
    make = models.CharField(max_length=50)
    customername = models.CharField(max_length=50)

    def __str__(self): 
        return self.make + ' ' + self.customername

class Employee(models.Model):
    make = models.CharField(max_length=50)
    empname = models.CharField(max_length=50)

    def __str__(self): 
        return self.make + ' ' + self.empname
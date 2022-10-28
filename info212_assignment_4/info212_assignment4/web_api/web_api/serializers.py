from rest_framework import serializers
from .models import Car, Customer, Employee

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'carmodel'] 


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'age', 'adress'] 


class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'branch', 'adress'] 
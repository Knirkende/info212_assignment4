from rest_framework import serializers
from .models import Car, Customer

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'carmodel', 'availability']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'booked_car']
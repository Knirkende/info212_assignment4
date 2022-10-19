from .models import Car, Customer
from rest_framework.response import Response
from .serializers import CarSerializer
from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def save_car(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
def update_car(request, id):
    try:
        theCar = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    serializer = CarSerializer(theCar, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_car(request, id):
    try:
        theCar = Car.objects.get(pk=id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    
    theCar.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#Ole-code start

@api_view(['PUT'])
def order_car(request, customer_id, car_id):
    try:
        the_car = Car.objects.get(pk=car_id)
        the_customer = Customer.objects.get(pk=customer_id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #TODO: Blocked until Customer model is defined + Car needs an availability field.    
    serializer = CarSerializer(the_car, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


"""
Implement an endpoint ‘order-car’ where a customer-id, car-id is passed as parameters.
The system must check that the customer with customer-id has not booked other cars. The
system changes the status of the car with car-id from ‘available’ to ‘booked’.
"""

"""
Implement an endpoint ‘cancel-order-car’ where a customer-id, car-id is passed as para-
meters. The system must check that the customer with customer-id has booked for the car.
If the customer has booked the car, the car becomes available.
"""
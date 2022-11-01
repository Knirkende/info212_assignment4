from .models import Car, Customer
from rest_framework.response import Response
from .serializers import CarSerializer, CustomerSerializer
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

@api_view(['GET'])
def order_car(request, customer_id, car_id):
    try:
        the_car = Car.objects.get(pk=car_id)
        the_customer = Customer.objects.get(pk=customer_id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if the_customer.booked_car != 'None':
        return Response(status=status.HTTP_404_NOT_FOUND) #TODO: something better.
    the_car.availability = 'booked'
    the_car.save()
    the_customer.booked_car = the_car.id
    the_customer.save()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def cancel_order_car(request, customer_id, car_id):
    try:
        the_car = Car.objects.get(pk=car_id)
        the_customer = Customer.objects.get(pk=customer_id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if the_customer.booked_car != str(the_car.id):
        return Response(status=status.HTTP_404_NOT_FOUND) #TODO: something better.
    the_car.availability = 'available'
    the_car.save()
    the_customer.booked_car = 'None'
    the_customer.save()
    return Response(status=status.HTTP_200_OK)
  
@api_view(['GET'])
def rent_car(request, customer_id, car_id):
    try:
        the_car = Car.objects.get(pk=car_id)
        the_customer = Customer.objects.get(pk=customer_id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if the_customer.booked_car != str(car_id):
        return Response(status=status.HTTP_404_NOT_FOUND) #TODO: something better.
    the_car.availability = 'rented'
    the_car.save()
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def return_car(request, customer_id, car_id, car_status):
    try:
        the_car = Car.objects.get(pk=car_id)
        the_customer = Customer.objects.get(pk=customer_id)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if the_customer.booked_car != str(the_car.id):
        return Response(status=status.HTTP_404_NOT_FOUND) #TODO: something better.
    if car_status == 'damaged':
        the_car.availability = 'damaged'
    else:
        the_car.availability = 'available'
    the_car.save()
    the_customer.booked_car = 'None'
    the_customer.save()
    return Response(status=status.HTTP_200_OK)
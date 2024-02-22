from django.http import JsonResponse
from django.shortcuts import render
from gpstracker import models
import gpsd
import serial

# Create your views here.

# models.Courier.objects.create(
#     name = 'Sanzhar',
#     phone = '87758155576',
#     type = '1',
#     xcoordination = None,
#     ycoordination = None
# )

def get_courier_coordinates(request, courier_id):

    try:
        courier = models.Courier.objects.get(id=courier_id)

        return JsonResponse({ "longitude" : courier.xcoordination , "latitude" : courier.ycoordination }, status=201)

    except Exception as e:
        return e
    

def update_courier_coordinates(request, courier_id):
    try:
        xcoordination = request.POST['longitude'] 
        ycoordination = request.POST['latitude']

        courier = models.Courier.objects.get(id=courier_id)
        courier.xcoordination = xcoordination
        courier.ycoordination = ycoordination
        courier.save()

        return JsonResponse({}, status=201)
    
    except Exception as e:
        return e
    
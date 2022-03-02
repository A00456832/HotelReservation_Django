from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import  NotFound
from rest_framework import status

from .models import Hotel
from .serializers import HotelSerializers



# Create your views here.
#def home(request):
 #   return HttpResponse("Hello World")


@api_view(['GET', 'POST'])
def Hotels_list(request):
    if request.method == 'GET':
        hotels_list = Hotel.objects.all()
        hotelSerializer = HotelSerializers(hotels_list, many=True)
        return Response(hotelSerializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        hotel_request = request.data
        hotel_request['finalCost'] = hotel_request['noDaysBooked'] * hotel_request['price']

        serialize_request_data = HotelSerializers(data=hotel_request)
        if serialize_request_data.is_valid():
            serialize_request_data.save()
        return Response({"Message": "Hotel name - {} has been added Successfully".format(hotel_request['name'])}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def Hotel_Details(request,pk):
    if request.method == 'GET':
        if Hotel.objects.filter(id=pk).exists():
            hotels_list = Hotel.objects.get(id=pk)
            print(hotels_list)
            hotelSerializer = HotelSerializers(hotels_list, many=False)
            return Response(hotelSerializer.data)
        else:
            raise NotFound(detail="hotel id - {} does not exist.".format(pk), code=404)

def error_404_view(request, exception=None):
    return HttpResponse("Invalid URL", status=404)




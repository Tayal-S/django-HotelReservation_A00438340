
from rest_framework import generics
from django.http import HttpResponse
from .models import Hotels
from .serializer import HotelSerializer
# Create your views here.

def Hello(request):
    return HttpResponse("Hello World")



class hotel_viewlist(generics.ListCreateAPIView):
    queryset = Hotels.objects.all()
    serializer_class = HotelSerializer
    
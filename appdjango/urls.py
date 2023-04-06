from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   
    path("Hello", views.Hello),
    path("hotels",views.hotel_viewlist.as_view(),name="HotelViewList")
]

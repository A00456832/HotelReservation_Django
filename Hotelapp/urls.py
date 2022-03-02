from django.urls import path
from . import views
from django.conf.urls import handler404
from django.contrib import admin

urlpatterns=[
   # path("home/", views.home, name="home"),
    path("hotel_list/", views.Hotels_list, name="hotelList"),
    path("hotel_list/<str:pk>", views.Hotel_Details, name="hotelDetails"),

]


handler404 = views.error_404_view





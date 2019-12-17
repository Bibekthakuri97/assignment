from django.contrib import admin
from django.urls import path
from timeteller.views import greet,today,timestamp

urlpatterns = [
    path('', greet),
    path('today', today),
    path('timestamp', timestamp)
]

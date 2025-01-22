from django.shortcuts import render
from rest_framework import viewsets
from .serializer import AdvertiseSerializer
from.models import AdvertiseModel
# Create your views here.


class AdvertiseViewsets(viewsets.ModelViewSet):
    queryset = AdvertiseModel.objects.all()
    serializer_class = AdvertiseSerializer


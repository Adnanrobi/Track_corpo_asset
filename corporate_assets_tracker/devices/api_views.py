from rest_framework import generics
from .models import Device
from .serializers import DeviceSerializer


class DeviceListAPIView(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

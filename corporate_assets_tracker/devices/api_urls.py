from django.urls import path
from .api_views import DeviceListAPIView, DeviceDetailAPIView

urlpatterns = [
    path("devices/", DeviceListAPIView.as_view(), name="api-device-list"),
    path("devices/<int:pk>/", DeviceDetailAPIView.as_view(), name="api-device-detail"),
]

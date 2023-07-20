from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.device_list, name='device_list'),
    path('<int:device_id>/', views.device_detail, name='device_detail'),
    path('<int:device_id>/checkout/', views.device_checkout, name='device_checkout'),
    # Add other URLs for create, update, delete, etc.
]
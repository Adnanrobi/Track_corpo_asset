from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.device_list, name='device_list'),
    path('<int:device_id>/', views.device_detail, name='device_detail'),
    path('<int:device_id>/checkout/', views.device_checkout, name='device_checkout'),
    # Add the URL pattern for the simulate_payment view
    path('<int:device_id>/payment/', views.simulate_payment, name='simulate_payment'),
]
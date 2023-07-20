from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('companies/', include('companies.urls')),
    path('employees/', include('employees.urls')),
    path('devices/', include('devices.urls')),
    path('api/', include('devices.api_urls')),  # Include the API URLs from the 'devices' app
]


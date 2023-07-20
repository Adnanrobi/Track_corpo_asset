from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('companies/', include('companies.urls')),
    path('employees/', include('employees.urls')),
    path('devices/', include('devices.urls')),
    # Add other URL patterns for your project
]
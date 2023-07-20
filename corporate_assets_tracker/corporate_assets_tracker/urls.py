from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="API Documentation")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/docs/", schema_view),
    path("companies/", include("companies.urls")),
    path("employees/", include("employees.urls")),
    path("devices/", include("devices.urls")),
    path(
        "api/", include("devices.api_urls")
    ),  # Include the API URLs from the 'devices' app
]

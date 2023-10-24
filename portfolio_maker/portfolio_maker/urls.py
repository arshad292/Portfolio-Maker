from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("user/", include("user_interface.urls")),
    path("admin/", admin.site.urls),
]
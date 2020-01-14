from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

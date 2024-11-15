"""
URL configuration for KarKhajana project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from carsworld.views import *
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('registration/',registration,name='registration'),
# ]

# urls.py

from rest_framework.documentation import include_docs_urls
from carsworld.views import CarListCreateView, CarDetailView, CarSearchView

urlpatterns = [
    path('api/cars/', CarListCreateView.as_view(), name='car-list-create'),
    path('api/cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
    path('api/cars/search/', CarSearchView.as_view(), name='car-search'),
    path('api/docs/', include_docs_urls(title='Car Management API')),
]

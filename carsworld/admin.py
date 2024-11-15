from django.contrib import admin

# Register your models here.

from carsworld.models import *

admin.site.register(Car)

admin.site.register(CarImage)
from django.contrib import admin
from .models import CarSpecification, CarPlan

# Register your models here.
admin.site.register(CarSpecification)
admin.site.register(CarPlan)

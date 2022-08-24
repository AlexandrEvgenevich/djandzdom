from django.contrib import admin
from .models import Sensor

# Register your models here.


@admin.register(Sensor)
class SensorsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

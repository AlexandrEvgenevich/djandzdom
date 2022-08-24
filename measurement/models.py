from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True, default='----')


class Measurement(models.Model):
    sensor = models.IntegerField()
    temperature = models.IntegerField()
    created_at = models.DateField(auto_now=True)

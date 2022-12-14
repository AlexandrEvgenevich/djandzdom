# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import SensorsSerializer, MeasurementSerializer, AdvSensorsSerializer
from rest_framework.views import APIView
from django.forms import model_to_dict
from rest_framework.generics import RetrieveAPIView


class AllSensorsView(APIView):
    def get(self, request):
        sens = Sensor.objects.all()
        ser = SensorsSerializer(sens, many=True)
        return Response(ser.data)

    def post(self, request):
        data = Sensor.objects.create(name=request.data['name'], description=request.data['description'])
        return Response({'post': model_to_dict(data)})


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = AdvSensorsSerializer

    def get_pk(self, pk):
        return Sensor.objects.get(pk=pk)

    def patch(self, request, pk):
        gpk = self.get_pk(pk)
        ser = SensorsSerializer(gpk, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response({'data': 'update'})
        return Response({'update': 'error'})


class MeasurementsView(APIView):
    def get(self, request):
        meas = Measurement.objects.all()
        ser = MeasurementSerializer(meas, many=True)
        return Response(ser.data)

    def post(self, request):
        sens = Sensor.objects.get(id=request.data['sensor'])
        meas = Measurement.objects.create(sensor=sens, temperature=request.data['temperature'])
        ser = MeasurementSerializer(meas, data=request.data)
        return Response({'XPEHb': 'XPEHb'})

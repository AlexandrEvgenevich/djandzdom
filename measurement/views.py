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

    # def get_pk(self, pk):
    #     return Sensor.objects.get(pk=pk)

    def get(self, request):
        meas = Measurement.objects.all()
        ser = MeasurementSerializer(meas, many=True)
        return Response(ser.data)

    def post(self, request):
        req = request.data
        meas = Measurement.objects.all()
        ser = AdvSensorsSerializer(meas, data=req)
        sens = Sensor.objects.filter(id=req['sensor'])
        ser.is_valid()
        ser.save()

        return Response({'XPEHb': 'XPEHb'})

    # def post(self, request):
    #     meas = Measurement.objects.all()
    #     ser = AdvSensorsSerializer(meas, data=request.data, many=True)
    #     print(request.data)
    #     if ser.is_valid():
    #         ser.save()
    #     return Response({'XPEHb': 'XPEHb'})
    #

    # def post(self, request):
        # gpk = self.get_pk(request.data['sensor'])
        # sens = Sensor.objects.get(pk=gpk)
        # sens = Sensor.objects.get(id=request.data['sensor'])


        # print(sens)
        # meas_ser = AdvSensorsSerializer(data=request.data)
        # print(meas_ser)
        # meas = Measurement.objects.all()
        # meas_ser = MeasurementSerializer(meas, data=request.data, many=True)
        # meas_advser = AdvSensorsSerializer(meas, data=request.data, many=True)
        #
        # if meas.is_valid():
        #     meas.save()
        #     return Response({'XPEHb': '___'})
        #

        # if meas_ser.is_valid():
        #     meas_ser.save()
        #     return Response({'XPEHb': '___'})
        #
        # sens = Sensor.objects.filter(id=request.data['sensor'])
        # sens2 = Sensor.objects.get(id=request.data['sensor'])
        # sens3 = request.data.get('sensor')
        # sens_ser = SensorsSerializer(sens, data=request.data, many=True, partial=True)
        # print(sens3)
        # print(sens_ser)
        #
        # if sens_ser.is_valid():
        #     sens_ser.save()
        #     return Response({'XPEHb': '___'})
        #
        # return Response({'XPEHb': 'XPEHb'})

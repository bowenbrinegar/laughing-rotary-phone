from rest_framework import generics, viewsets, status
from django.db.models import Q
from .db.models import *
from .serializers import *
from rest_framework.response import Response
import json

class FlightCreateView(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class SpeedDataCreateView(generics.ListCreateAPIView):
    queryset = SpeedData.objects.all()
    serializer_class = SpeedDataSerializer

class PositionDataCreateView(generics.ListCreateAPIView):
    queryset = PositionData.objects.all()
    serializer_class = PositionDataSerializer

class HoopsBundleCreateView(generics.ListCreateAPIView):
    queryset = HoopsBundle.objects.all()
    serializer_class = HoopsBundleSerializer

class HoopDataCreateView(generics.ListCreateAPIView):
    queryset = HoopData.objects.all()
    serializer_class = HoopDataSerializer

class AsteriodsBundleCreateView(generics.ListCreateAPIView):
    queryset = AsteriodsBundle.objects.all()
    serializer_class = AsteriodsBundleSerializer

class AsteriodDataCreateView(generics.ListCreateAPIView):
    queryset = AsteriodData.objects.all()
    serializer_class = AsteriodDataSerializer

class FlightMassView(viewsets.ViewSet):
    def retrieve(self, request, flight_id=None):
        flight = Flight.objects.filter(id=flight_id).prefetch_related("speed", "position", "hoops", "asteriods").first()
        
        wrapper = {}

        wrapper['flight'] = flight.as_dict_response()
        wrapper['speed'] = [item.as_dict_response() for item in flight.speed.all()]
        wrapper['position'] = [item.as_dict_response() for item in flight.position.all()]
        wrapper['asteriod_bundles'] = [item.as_dict_response() for item in flight.asteriods.all()]
        wrapper['hoop_bundles'] = [item.as_dict_response() for item in flight.hoops.all()]
        
        asteriodBundle = wrapper['asteriod_bundles'] 
        for i in range(len(asteriodBundle)):
            asteriods = AsteriodData.objects.filter(asteriod_id=asteriodBundle[i]["id"])
            wrapper['asteriod_bundles'][i]['asteriods'] = []
            for j in range(len(asteriods)):
                wrapper['asteriod_bundles'][i]['asteriods'].append(asteriods[j].as_dict_response())

        hoopBundle = wrapper['hoop_bundles'] 
        for i in range(len(hoopBundle)):
            hoops = HoopData.objects.filter(hoop_id=hoopBundle[i]["id"])
            wrapper['hoop_bundles'][i]['hoops'] = []
            for j in range(len(hoops)):
                wrapper['hoop_bundles'][i]['hoops'].append(hoops[j].as_dict_response())

        return Response(wrapper, status=status.HTTP_202_ACCEPTED)

class FlightAllView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

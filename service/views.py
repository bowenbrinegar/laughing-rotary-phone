from rest_framework import generics, viewsets, status
from django.db.models import Q
from .db.models import Flight, FlightTracker
from .serializers import FlightSerializer, FlightTrackerSerializer
from rest_framework.response import Response

class FlightCreateView(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = FlightSerializer

    def get_queryset(self):
        return Flight.objects.all()

class FlightViewSet(viewsets.ViewSet):
    def retrieve(self, request, id=None):
        curr = Flight.objects.get(id=id)
        if curr:
            return Response(curr.as_dict_response(), status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"object": "not_found"}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, id=None):
        incoming = request.data
        obj = Flight.objects.filter(id=id).update(**incoming)
    
        if obj == 1:
            return Response({"success": 'driod found and updated'}, status=status.HTTP_200_OK)
        else:
            return Response({"error": 'these are not the driods you are looking for'}, status=status.HTTP_400_BAD_REQUEST)
       
    def partial_update(self, request, id=None):
        incoming = request.data
        obj = Flight.objects.filter(id=id).update(**incoming)
    
        if obj == 1:
            return Response({"success": 'driod found and updated'}, status=status.HTTP_200_OK)
        else:
            return Response({"error": 'these are not the driods you are looking for'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, id=None):
        instance = Flight.objects.get(id=id)

        if instance:
            instance.delete()
            return Response({"destroyed": True}, status=status.HTTP_200_OK)
        else:
            return Response({"object": "not_found"}, status=status.HTTP_404_NOT_FOUND)

class FlightAllView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class FlightTrackerCreateView(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = FlightTrackerSerializer

    def get_queryset(self):
        return FlightTracker.objects.all()


class FlightDataAllView(viewsets.ModelViewSet):
    lookup_field = 'flight_id'
    serializer_class = FlightTrackerSerializer

    def get_queryset(self):
        return FlightTracker.objects.all()

class FlightTrackerViewSet(viewsets.ViewSet):
    def retrieve(self, request, id=None):
        curr = FlightTracker.objects.get(id=id)
        if curr:
            return Response(curr.as_dict_response(), status=status.HTTP_202_ACCEPTED)
        else:
            return Response({"object": "not_found"}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, id=None):
        incoming = request.data
        obj = FlightTracker.objects.filter(id=id).update(**incoming)
    
        if obj == 1:
            return Response({"success": 'driod found and updated'}, status=status.HTTP_200_OK)
        else:
            return Response({"error": 'these are not the driods you are looking for'}, status=status.HTTP_400_BAD_REQUEST)
       
    def partial_update(self, request, id=None):
        incoming = request.data
        obj = FlightTracker.objects.filter(id=id).update(**incoming)
    
        if obj == 1:
            return Response({"success": 'driod found and updated'}, status=status.HTTP_200_OK)
        else:
            return Response({"error": 'these are not the driods you are looking for'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, id=None):
        instance = FlightTracker.objects.get(id=id)

        if instance:
            instance.delete()
            return Response({"destroyed": True}, status=status.HTTP_200_OK)
        else:
            return Response({"object": "not_found"}, status=status.HTTP_404_NOT_FOUND)

class FlightTrackerAllView(viewsets.ModelViewSet):
    queryset = FlightTracker.objects.all()
    serializer_class = FlightTrackerSerializer
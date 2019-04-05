from django.contrib import admin
from django.urls import path
from .views import FlightCreateView, FlightViewSet, FlightAllView, FlightTrackerCreateView, FlightTrackerViewSet, FlightTrackerAllView, FlightDataAllView

urlpatterns = [
    path('api/v1/beats/beer/battle_start_glactica/create_flight', FlightCreateView.as_view(), name='flight_create_view'),
    path('api/v1/beats/beer/battle_start_glactica/retrieve_flight/<id>', FlightViewSet.as_view({'get': 'retrieve'}), name='flight_retrieve_view'),
    path('api/v1/beats/beer/battle_start_glactica/update_flight/<id>', FlightViewSet.as_view({'put': 'update'}), name='flight_update_view'),
    path('api/v1/beats/beer/battle_start_glactica/partial_update_flight/<id>', FlightViewSet.as_view({'patch': 'partial_update'}), name='flight_update_view'),
    path('api/v1/beats/beer/battle_start_glactica/destroy_flight/<id>', FlightViewSet.as_view({"delete": 'destroy'}), name='flight_update_view'),
    path('api/v1/beats/beer/battle_start_glactica/all_flight', FlightAllView.as_view({'get': 'list'}), name='flight_all_view'),
    path('api/v1/beats/beer/battle_start_glactica/create_flight/data_point', FlightTrackerCreateView.as_view(), name='flight_create_view'),
    path('api/v1/beats/beer/battle_start_glactica/retieve_flight_data/<id>', FlightDataAllView.as_view({'get':'list'}), name='retrieve_all_flight_data'),
    path('api/v1/beats/beer/battle_start_glactica/retrieve_flight/data_point/<id>', FlightTrackerViewSet.as_view({'get': 'retrieve'}), name='flight_retrieve_view'),
    path('api/v1/beats/beer/battle_start_glactica/update_flight/data_point/<id>', FlightTrackerViewSet.as_view({'put': 'update'}), name='flight_update_view'),
    path('api/v1/beats/beer/battle_start_glactica/partial_update_flight/data_point/<id>', FlightTrackerViewSet.as_view({'patch': 'partial_update'}), name='flight_update_view'),
    path('api/v1/beats/beer/battle_start_glactica/destroy_flight/data_point/<id>', FlightTrackerViewSet.as_view({"delete": 'destroy'}), name='flight_update_view'),
    path('api/v1/beats/beer/battle_start_glactica/all_flight/data_point', FlightTrackerAllView.as_view({'get': 'list'}), name='flight_all_view'),
]


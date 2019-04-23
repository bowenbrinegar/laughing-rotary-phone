from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/beats/beer/battle_star_galactica/create_flight', FlightCreateView.as_view(), name='flight_create_view'),
    path('api/v1/beats/beer/battle_star_galactica/create_speed_data', SpeedDataCreateView.as_view(), name='speed_create_view'),
    path('api/v1/beats/beer/battle_star_galactica/create_position_data', PositionDataCreateView.as_view(), name='position_create_view'),
    path('api/v1/beats/beer/battle_star_galactica/create_hoops_bundle', HoopsBundleCreateView.as_view(), name='hoops_bundle_create_view'),
    path('api/v1/beats/beer/battle_star_galactica/create_hoop_data', HoopDataCreateView.as_view(), name='hoop_data_create_view'),
    path('api/v1/beats/beer/battle_star_galactica/create_asteriods_bundle', AsteriodsBundleCreateView.as_view(), name='asteriods_bundle_create_view'),
    path('api/v1/beats/beer/battle_star_galactica/create_asteriod_data', AsteriodDataCreateView.as_view(), name='asteriod_data_create_view'),
    path('api/v1/beats/beer/battle_star_galactica/get_massive_flight/<flight_id>', FlightMassView.as_view({'get': 'retrieve'}), name='get_massive_flight'),
    path('api/v1/beats/beer/battle_star_galactica/all_flights', FlightAllView.as_view({'get': 'list'}), name='flight_all_view'),
]
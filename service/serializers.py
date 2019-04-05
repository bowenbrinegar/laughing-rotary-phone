from rest_framework import serializers
from .db.models import Flight, FlightTracker

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = [
            'id',
            'created',
            'username',
        ]

    def create(self, validated_data):
        return Flight.objects.create(**validated_data)

    def update(self, instance, validated_data):
        updated = validated_data.save()
        return updated

class FlightTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlightTracker
        fields = [
            'id',
            'created',
            'x_pos',
            'y_pos',
            'avg_dist_to_potential_collision',
            'flight_id'
        ]

    def create(self, validated_data):
        return FlightTracker.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        updated = validated_data.save()
        return updated
    
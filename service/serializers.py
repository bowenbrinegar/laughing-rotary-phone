from rest_framework import serializers
from .db.models import *

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = [
            'id',
            'created',
            'username',
            'score',
            'livesLeft',
            'timeLeft'
        ]

    def create(self, validated_data):
        return Flight.objects.create(**validated_data)

    def update(self, instance, validated_data):
        updated = validated_data.save()
        return updated

class SpeedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeedData
        fields = [
            'id',
            'created',
            'speed',
            'time',
            'flight_id'
        ]

    def create(self, validated_data):
        return SpeedData.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        updated = validated_data.save()
        return updated


class PositionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PositionData
        fields = [
            'id',
            'created',
            'x_pos',
            'y_pos',
            'time',
            'flight_id'
        ]

    def create(self, validated_data):
        return PositionData.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        updated = validated_data.save()
        return updated
        
class HoopsBundleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoopsBundle
        fields = [
            'id',
            'created',
            'time',
            'flight_id'
        ]

    def create(self, validated_data):
        return HoopsBundle.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        updated = validated_data.save()
        return updated

class HoopDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoopData
        fields = [
            'id',
            'created',
            'x_pos',
            'y_pos',
            'hoop_id'
        ]

    def create(self, validated_data):
        return HoopData.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        updated = validated_data.save()
        return updated


class AsteriodsBundleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsteriodsBundle
        fields = [
            'id',
            'created',
            'time',
            'flight_id'
        ]

    def create(self, validated_data):
        return AsteriodsBundle.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        updated = validated_data.save()
        return updated

class AsteriodDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsteriodData
        fields = [
            'id',
            'created',
            'x_pos',
            'y_pos',
            'asteriod_id'
        ]

    def create(self, validated_data):
        return AsteriodData.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        updated = validated_data.save()
        return updated


class Parent(serializers.Serializer):
    flight = FlightSerializer(many=False, read_only=True)
    speed = SpeedDataSerializer(many=True, read_only=True)
    position = PositionDataSerializer(many=True, read_only=True)

    def to_internal_value(self, instance):
        response = super().to_internal_value(instance)
        return response
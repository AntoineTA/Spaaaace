from rest_framework import serializers
from .models import *

class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        exclude = []

class SatelliteSerializer(serializers.ModelSerializer):
    operator = OperatorSerializer()

    class Meta:
        model = Satellite
        exclude = []

    def create(self, validated_data):
        operator_data = self.initial_data.get('operator')
        satellite = Satellite(**{**validated_data, 
                                 'operator': Operator.objects.get(pk=operator_data['id'])
                                })
        satellite.save()
        return satellite
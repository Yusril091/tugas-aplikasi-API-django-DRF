# dalam file serializers.py di dalam aplikasi car_dealer

from rest_framework import serializers
from .models import Dealer, Car

class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

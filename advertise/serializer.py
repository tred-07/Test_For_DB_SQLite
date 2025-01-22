from rest_framework import serializers
from .models import AdvertiseModel

class AdvertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertiseModel
        fields = ('title', 'description', 'image')
# serializers.py
from rest_framework import serializers
from .models import Car, CarImage

class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ['id', 'image', 'uploaded_at']

class CarSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'title', 'description', 'tags', 'images', 'created_at', 'updated_at']

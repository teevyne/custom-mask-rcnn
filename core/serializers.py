# serializers.py

from rest_framework import serializers
from .models import ImagePath

class ImagePathSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagePath
        fields = '__all__'

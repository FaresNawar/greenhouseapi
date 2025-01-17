from rest_framework import serializers
from project.models import Status

class statusSerializer(serializers.ModelSerializer):
    class Meta:
        model=Status
        fields=['pk','image','predict_class','predict_presntage']
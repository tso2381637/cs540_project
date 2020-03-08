from rest_framework import serializers
from .models import AllCleanedCrashData
from django.conf import settings

class AllCleanedCrashDataSerializer(serializers.ModelSerializer):

    latitude = serializers.DecimalField(max_digits=8, decimal_places=6)
    longitude = serializers.DecimalField(max_digits=8, decimal_places=6)
    crash_time = serializers.DateTimeField(format=settings.DATETIME_FORMAT, required=False)

    class Meta:
        model = AllCleanedCrashData
        fields = '__all__'

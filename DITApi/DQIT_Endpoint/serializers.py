# serializers.py
from rest_framework import serializers
from .models import DataQualityIssues,Facilities, EmailSetup, DataSyncSettings


class DataQualityIssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataQualityIssues
        fields = '__all__'


class FacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = '__all__'

class EmailSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSetup
        fields = '__all__'

class DataSyncSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSyncSettings
        fields = '__all__'
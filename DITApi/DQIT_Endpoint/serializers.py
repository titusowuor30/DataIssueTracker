# serializers.py
from rest_framework import serializers
from .models import DataQualityIssues,Facilities, EmailSetup, DataSyncSettings


class DataQualityIssuesSerializer(serializers.ModelSerializer):
    facility_name = serializers.CharField(source='facility.facility_name', read_only=True)
    country = serializers.CharField(source='facility.country', read_only=True)

    class Meta:
        model = DataQualityIssues
        fields = ['id', 'patient_id', 'date_of_entry', 'inconsistency', 'action_taken', 'date_action_taken', 'country','facility_name']



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

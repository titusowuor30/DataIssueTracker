from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DataQualityIssues

class DataIssuesStats(APIView):

    def get(self,request, format=None):
        all_issues=DataQualityIssues.objects.count()
        pending_count=DataQualityIssues.objects.filter(action_taken='Pending').count()
        corrected_count=DataQualityIssues.objects.filter(action_taken='Entry Corrected').count()
        matching_count=DataQualityIssues.objects.filter(action_taken='Data Matches Source Document').count()
        available_count=DataQualityIssues.objects.filter(action_taken='Data Already Available').count()
        no_data_count=DataQualityIssues.objects.filter(action_taken='No Data Needed').count()

        data={
            'pending':pending_count,
            'corrected':corrected_count,
            'matching':matching_count,
            'available':available_count,
            'no_data':no_data_count,
            'all_issues':all_issues
            }
        return Response(data)
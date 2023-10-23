from rest_framework import generics
from rest_framework.response import Response
from DQIT_Endpoint.models import DataQualityIssues,Facilities
from DQIT_Endpoint.serializers import DataQualityIssuesSerializer
from datetime import date,datetime
from django.db.models import Count

class DataQualityIssuesAnalyticsView(generics.ListAPIView):
    serializer_class = DataQualityIssuesSerializer

    def list(self, request, *args, **kwargs):
        # Handle user filters
        facility = request.query_params.get('facility', None)
        facility=Facilities.objects.filter(facility_name=facility).first()
        selected_action = request.query_params.get('action_taken', None)
        selected_year = request.query_params.get('year', None)

        # Get the current year
        current_year = date.today().year
        if selected_year:
            current_year=selected_year

        # Query to count data quality issues by action_taken for the whole year
        analytics_whole_year = DataQualityIssues.objects.filter(date_of_entry__year=current_year)
        if facility:
            analytics_whole_year = analytics_whole_year.filter(facility=facility)
        if selected_action:
            analytics_whole_year = analytics_whole_year.filter(action_taken=selected_action)

        analytics_whole_year = analytics_whole_year.values('action_taken').annotate(count=Count('id')).order_by('action_taken')

        # Query to count data quality issues by action_taken for each month in the current year
        analytics_by_month = DataQualityIssues.objects.filter(date_of_entry__year=current_year)
        if facility:
            analytics_by_month = analytics_by_month.filter(facility=facility)
        if selected_action:
            analytics_by_month = analytics_by_month.filter(action_taken=selected_action)

        analytics_by_month = analytics_by_month.values('action_taken', 'date_of_entry__month').annotate(count=Count('id')).order_by('date_of_entry__month', 'action_taken')

        # Create response data
        response_data = {
            'analytics_whole_year': analytics_whole_year,
            'analytics_by_month': analytics_by_month,
        }

        return Response(response_data)

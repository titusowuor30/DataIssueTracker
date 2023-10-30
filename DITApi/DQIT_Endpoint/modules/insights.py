from rest_framework import generics
from rest_framework.response import Response
from DQIT_Endpoint.models import DataQualityIssues,Facilities
from DQIT_Endpoint.serializers import DataQualityIssuesSerializer
from datetime import date,datetime
from django.db.models import Count
from collections import defaultdict


class DataQualityIssuesAnalyticsView(generics.ListAPIView):
    serializer_class = DataQualityIssuesSerializer

    def list(self, request, *args, **kwargs):
        # Handle user filters
        facility = request.query_params.get('facility', None)
        facility=Facilities.objects.filter(facility_name=facility).first()
        selected_action = request.query_params.get('action_taken', None)
        selected_year = request.query_params.get('year', None)


        # Prepare a base queryset for the selected year
        base_queryset = DataQualityIssues.objects.filter(date_of_entry__isnull=False,facility__in=request.user.facilities.all()) if request.user.role.role_name !='Admin' else DataQualityIssues.objects.filter(date_of_entry__isnull=False)
        if facility and facility !='All':
            base_queryset = base_queryset.filter(facility=facility)
        if selected_action and selected_action !='All':
            base_queryset = base_queryset.filter(action_taken=selected_action)
        # Get the current year
        if selected_year and selected_year !='All':
            base_queryset=base_queryset.filter(date_of_entry__year=selected_year)

        analytics_by_year = base_queryset.values('date_of_entry').annotate(count=Count('id')).order_by('-date_of_entry__year')

        # Count data quality issues by year and month
        data = defaultdict(lambda: defaultdict(int))
        for issue in analytics_by_year:
            year = issue['date_of_entry'].year
            month = issue['date_of_entry'].month
            data[year][month] +=issue['count']

        # Generate the desired data format
        series = []
        for year, months in data.items():
            series.append({
                "name": str(year),
                "data": [months.get(i, 0) for i in range(1, 13)],  # 1 to 12 months
            })


        # Calculate the conversion ratio for 'Pending' to other actions
        pending_count = base_queryset.filter(
            action_taken='Pending'
        )
        
        converted_count = base_queryset.filter(
            action_taken__in=['Entry Corrected', 'Data Matches Source Document', 'Data Already Available', 'No Data Needed']
        )
        
        pending_count = pending_count.count()
        converted_count = converted_count.count()

        # Calculate the conversion ratio
        conversion_ratio = 0.0
        if pending_count > 0:
            conversion_ratio = (converted_count / pending_count)*100

        response_data = {
            'series': series,
            'conversion_ratio': float(f"{conversion_ratio:.2f}"),
        }

        return Response(response_data)

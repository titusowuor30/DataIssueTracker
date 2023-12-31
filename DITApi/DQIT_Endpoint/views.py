from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from django.http import Http404
from .models import DataQualityIssues,Facilities,EmailSetup,DataSyncSettings
from .utils import DataImporter
from django.db.models import Q
from .serializers import DataQualityIssuesSerializer,FacilitiesSerializer,EmailSetupSerializer,DataSyncSettingsSerializer
import logging
logger = logging.getLogger('ditapi_logger')
class DataQualityIssuesEndpoints(APIView):

    def process_issues(self, data):
        for id in data:
            yield id  # Yield the processed ID, for memory effieciency in case of big data

    def post(self, request, format=None):
        ids = request.data['data_ids']
        processed_ids=self.process_issues(ids)
        ##print(list(processed_ids))
        for id in processed_ids:
            issue = self.get_object(id)
            issue.action_taken =request.data['action']
            issue.save()
        return Response('success!', status=status.HTTP_201_CREATED)

    def get_object(self, pk):
        try:
            return DataQualityIssues.objects.get(pk=pk)
        except DataQualityIssues.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            issue=self.get_object(pk)
            serializer = DataQualityIssuesSerializer(issue)
            return Response(serializer.data)

        query_params = request.query_params
        patient_id = query_params.get('patient_id',None)
        date_of_entry = query_params.get('date_of_entry',None)
        inconsistency = query_params.get('inconsistency',None)
        country = query_params.get('country',None)
        facility = query_params.get('facility',None)


        issues = DataQualityIssues.objects.filter(facility__in=request.user.facilities.all()) if request.user.role.role_name !='Admin' else DataQualityIssues.objects.all()

        if patient_id:
            issues = issues.filter(patient_id=patient_id)
        if date_of_entry:
            issues = issues.filter(date_of_entry=date_of_entry)
        if inconsistency:
            issues = issues.filter(inconsistency__icontains=inconsistency)
        if facility and facility !='All':
            issues = issues.filter(facility__facility_name=facility)
        if country and country !='All':
            issues = issues.filter(facility__country=country)

        paginator = LimitOffsetPagination()
        paginator.default_limit = 10
        result_page = paginator.paginate_queryset(issues, request)
        serializer = DataQualityIssuesSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def put(self, request, pk, format=None):
        issue = self.get_object(pk)
        if issue:
            issue.action_taken=request.data['action']
            issue.save()
            return Response('Success!')
        return Response('Error updating issue', status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        issue = self.get_object(pk)
        issue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FacilitiesEndpoints(APIView):

    def post(self, request, format=None):
        serializer = Facilities(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, pk):
        try:
            return Facilities.objects.get(pk=pk)
        except Facilities.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            facility=self.get_object(pk)
            serializer = FacilitiesSerializer(facility)
            return Response(serializer.data)

        query_params = request.query_params
        facility_code = query_params.get('facility_code',None)
        facility_name = query_params.get('facility_name',None)

        facilities = Facilities.objects.all()

        if facility_code:
            facilities = facilities.filter(facility_code=facility_code)
        if facility_name:
            facilities = facilities.filter(facility_name=facility_name)

        paginator = LimitOffsetPagination()
        paginator.default_limit = 100
        result_page = paginator.paginate_queryset(facilities, request)
        serializer = FacilitiesSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def put(self, request, pk, format=None):
        issue = self.get_object(pk)
        serializer = FacilitiesSerializer(issue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        issue = self.get_object(pk)
        issue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmailSetupEndpoints(APIView):

    def post(self, request, format=None):
        serializer = EmailSetup(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self):
        try:
            return EmailSetup.objects.first()
        except EmailSetup.DoesNotExist:
            raise Http404

    def get(self, request,format=None):
            setup=self.get_object()
            serializer = EmailSetupSerializer(setup)
            return Response(serializer.data)


    def put(self, request, format=None):
        setup = self.get_object()
        serializer = EmailSetupSerializer(setup, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        setup = self.get_object()
        setup.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DataSyncSetupEndpoints(APIView):

    def post(self, request, format=None):
        serializer = DataSyncSettings(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self):
        try:
            return DataSyncSettings.objects.first()
        except DataSyncSettings.DoesNotExist:
            raise Http404

    def get(self, request,format=None):
            setup=self.get_object()
            serializer = DataSyncSettingsSerializer(setup)
            return Response(serializer.data)


    def put(self, request, format=None):
        setup = self.get_object()
        serializer = DataSyncSettingsSerializer(setup, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        setup = self.get_object()
        setup.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SyncDataView(APIView):
    def post(self,request,*args,**kwargs):
        try:
            logger.info("Data sync active...")
            data_sync=DataSyncSettings.objects.first()
            data_importer = DataImporter(data_sync.data_issues_folder_url)
            data_importer.check_for_new_files(facility_file_path=data_sync.faclity_list_csv_path)
        except Exception as e:
           logger.error(e)
           return Response(f'An error occured! {str(e)}')
        return Response('Data sync running...')
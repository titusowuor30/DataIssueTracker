from django.urls import path
from .views import DataQualityIssuesEndpoints,FacilitiesEndpoints,EmailSetupEndpoints,DataSyncSetupEndpoints
from .stats import DataIssuesStats
urlpatterns = [
    #data issues
    path('data_issues/', DataQualityIssuesEndpoints.as_view(), name='data-quality-issues-list'),
    path('data_issues/<int:pk>/', DataQualityIssuesEndpoints.as_view(), name='data-quality-issues-detail'),
    #facilities
    path('facilities/', FacilitiesEndpoints.as_view(), name='facility-list'),
    path('facilities/<int:pk>/', FacilitiesEndpoints.as_view(), name='facility-detail'),
    #email setup
    path('email_setup/',EmailSetupEndpoints.as_view(), name='email-setup'),
    #data sync setup
    path('data_sync_setup/', DataSyncSetupEndpoints.as_view(), name='data-sync-setup'),

    #stats
    path('data_issue_stats/', DataIssuesStats.as_view(), name='data-issue-stats'),
]
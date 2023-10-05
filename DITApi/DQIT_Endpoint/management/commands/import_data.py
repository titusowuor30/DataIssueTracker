from django.core.management.base import BaseCommand
from DQIT_Endpoint.utils import DataImporter  # Import your DataImporter class
from DQIT_Endpoint.models import DataSyncSettings

class Command(BaseCommand):
    help = 'Import data from Excel and CSV files in a folder using DataImporter'

    def handle(self, *args, **options):
        print("Data sync active...")
        sync_setup=DataSyncSettings.objects.first()
        data_importer = DataImporter(sync_setup.data_issues_folder_url)
        # Run the data importer periodically (e.g., every 1 min)
        data_importer.check_for_new_files(facility_file_path=sync_setup.faclity_list_csv_path,duration=sync_setup.data_sync_frequency)

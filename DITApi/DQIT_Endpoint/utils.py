import os
import time
import pandas as pd
from django.db import IntegrityError
from .models import DataQualityIssues,Facilities
from datetime import datetime

class DataImporter:
    def __init__(self, data_folder):
        self.data_folder = data_folder
    def import_data_from_excel(self,file_path,facility_file_path,df=pd.DataFrame([])):
        #try:
        # Read the Excel file into a Pandas DataFrame
        facilities=Facilities.objects.all()
        if len(facilities) > 0:
            for _, row in df.iterrows():
                facility=facilities.filter(facility_code=row['Facility']).first()
                if facility is not None:
                    date_str=str(str(row['Date of Entry']).split(' ')[0])
                    issues={
                        'patient_id':row['Patient ID'],
                        'facility':facility,
                        'date_of_entry':pd.to_datetime(date_str, format='%Y-%m-%d').date(),
                        'inconsistency':row['Inconsistency'],
                        'action_taken':'Pending',
                        'date_action_taken':datetime.utcnow().date(),
                    }
                    _,created=DataQualityIssues.objects.get_or_create(
                        patient_id=row['Patient ID'],
                        date_of_entry=pd.to_datetime(str(date_str), format='%Y-%m-%d').date(),
                        inconsistency=row['Inconsistency'],
                        defaults=issues,
                        )
                    time.sleep(1)
            print(f"Data imported from {file_path} successfully.")
            new_file_name = file_path.replace('.xlsx', '_processed.xlsx') if 'xlsx' in file_path else file_path.replace('.csv',  '_processed.csv')
            os.rename(file_path, new_file_name)
        else:
            #sync facilities
            df_facility=pd.read_excel(facility_file_path) if 'xlsx' in facility_file_path else pd.read_csv(facility_file_path)
            for _, row in df_facility.iterrows():
                data={
                    'facility_code':row['ID'],
                    'facility_name':row['HospitalName'],
                    'country':row['country']
                }
                _,created=Facilities.objects.get_or_create(
                    facility_code=row['ID'],
                    defaults=data
                    )
            print(f"Facilities imported successfully.")
        #     print(f"Error importing data from {file_path}: {str(e)}")

    def generate_data_from_files(self):
        for filename in os.listdir(self.data_folder):
            if filename.endswith('.xlsx') and 'processed' not in filename:
                file_path = os.path.join(self.data_folder, filename)
                yield pd.read_excel(file_path),file_path
                time.sleep(1)
            else:
                if filename.endswith('.csv') and 'processed' not in filename:
                    file_path = os.path.join(self.data_folder, filename)
                    yield pd.read_csv(file_path),file_path
                    time.sleep(1)
        else:
            print('All files processed')

    def check_for_new_files(self,facility_file_path):
        for df, file_path in self.generate_data_from_files():
            df.drop_duplicates(inplace=True)#drop duplicates
            df.dropna(subset=['Inconsistency'],inplace=True)#drop rows where inconsistency is null
            print(df.shape)
            self.import_data_from_excel(file_path,facility_file_path,df)



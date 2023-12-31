import os
import time
import pandas as pd
from django.db import IntegrityError
from .models import DataQualityIssues,Facilities
from datetime import datetime
from user_agents import parse
import threading
import json
import os
from django.http import JsonResponse
from DQIT_Endpoint.modules.custom_email_backend import DQITSEmailBackend
from django.http import HttpRequest
import logging
logger = logging.getLogger('ditapi_logger')
def get_client_info(request):
    client_ip = request.META.get('REMOTE_ADDR', None)

    # Parse the user-agent string to get device and OS information
    user_agent = request.META.get('HTTP_USER_AGENT', None)
    if user_agent:
        user_agent_info = parse(user_agent)
        device = user_agent_info.device.family
        os = user_agent_info.os.family
        if device =='Other':
            device='Unknown Computer'
    # Perform your authentication and login logic here

    # Respond to the client or store the information as needed
    response = {"ip:":client_ip,"device:":device,"os:": os}
    return JsonResponse(response)

class DataImporter:
    def __init__(self, data_folder):
        self.data_folder = data_folder
        self.request=HttpRequest()
        data=os.environ.get('REQUEST_DATA',{})
        jsondata=json.loads(data)
        self.request.META=jsondata
        #logger.debug(self.request.META)
    def import_data_from_excel(self,file_path,facility_file_path,df=pd.DataFrame([])):
        try:
            # Read the Excel file into a Pandas DataFrame
            facilities=Facilities.objects.all()
            user_facility=None
            faclity_user=None
            if len(facilities) > 0:
                for _, row in df.iterrows():
                    facility=facilities.filter(facility_code=str(row['Facility'])).first()
                    if facility != None:
                        logger.info(f"facility -> {facility.facility_code}:{facility.facility_name}")
                        user_facility=facility
                        faclity_user=user_facility.customuser_set.first() 
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
                    else:
                        emailsent=0
                        logger.info(f"Skipping faclity no match found for Facility code -> {row['Facility']}")
                        subject="Facilty Not Matched Alert!"
                        message=f"Skipping data import for faclity ,no match found for Facility code -> {row['Facility']}"
                        if emailsent == 1:
                            emailthread=threading.Thread(target=DQITSEmailBackend(request=self.request,subject=subject,body=message,to=[faclity_user.email if faclity_user else 'titusowuor30@gmail.com',"titusowuor30@gmail.com",],attachments=[]).send_email(),name='EmailThread')
                            emailthread.daemon=True
                            emailthread.start()
                            logger.debug("Email thread started!")
                        emailsent+=1
                        continue #move to the next facility
                logger.info(f"Data imported from {file_path} successfully.")
                #Notify user 
                #print("Processing login mail")
                subject="New Issues Alert!"
                message=f"Dear {faclity_user.email if faclity_user else 'titusowuor30@gmail.com'},\n\n<br/>New data quality issues for facility {user_facility.facility_code}, {user_facility.facility_name}, have been uploaded into the DQITs portal, please login and check!"
                emailthread=threading.Thread(target=DQITSEmailBackend(request=self.request,subject=subject,body=message,to=[faclity_user.email if faclity_user else 'titusowuor30@gmail.com',"titusowuor30@gmail.com",],attachments=[]).send_email(),name='EmailThread')
                emailthread.daemon=True
                emailthread.start()
                logger.debug("Email thread started!")
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
                logger.info(f"Facilities imported successfully.")
        except Exception as e:
            subject="DQITs encountered an error while importing data"
            message=f"Error importing data from {file_path}: {str(e)}, please alert your system admin!"
            emailthread=threading.Thread(target=DQITSEmailBackend(request=self.request,subject=subject,body=message,to=[faclity_user.email if faclity_user else 'titusowuor30@gmail.com',"titusowuor30@gmail.com",],attachments=[]).send_email(),name='EmailThread')
            emailthread.daemon=True
            emailthread.start()
            logger.debug("Email thread started!")
            logger.error(f"Error importing data from {file_path}: {str(e)}")

    def generate_data_from_files(self):
        try:
            for filename in sorted(os.listdir(self.data_folder)):
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
                logger.info('All files processed')
        except Exception as e:
            logger.error(f"{e}")

    def check_for_new_files(self,facility_file_path):
        try:
            for df, file_path in self.generate_data_from_files():
                df.drop_duplicates(inplace=True)#drop duplicates
                #remove NATypes(Not-a-Timezone value)
                na_columns = df.columns[df.isna().any()].tolist()#nat col values
                na_count=df[na_columns].isna().sum()
                logger.warning(f"NATypes found -> count:{na_count}")
                #df['Date of Entry'] = df['Date of Entry'].fillna(pd.Timestamp('today'))# fill with current timestamp
                logger.info(f"dropping rows with NATypes")
                df.dropna(subset=['Inconsistency','Date of Entry'],inplace=True)#drop rows where inconsistency is null
                logger.info("rows dropped!")
                self.import_data_from_excel(file_path,facility_file_path,df)
            else:
                logger.info('All files processed')
        except Exception as e:
            logger.error(f"{e}")

    def check_for_new_files(self,facility_file_path):
        try:
            for df, file_path in self.generate_data_from_files():
                df.drop_duplicates(inplace=True)#drop duplicates
                #remove NATypes(Not-a-Timezone value)
                na_columns = df.columns[df.isna().any()].tolist()#nat col values
                na_count=df[na_columns].isna().sum()
                logger.warning(f"NATypes found -> count:{na_count}")
                #df['Date of Entry'] = df['Date of Entry'].fillna(pd.Timestamp('today'))# fill with current timestamp
                logger.info(f"dropping rows with NATypes")
                df.dropna(subset=['Inconsistency','Date of Entry'],inplace=True)#drop rows where inconsistency is null
                logger.info("rows dropped!")
                self.import_data_from_excel(file_path,facility_file_path,df)
        except Exception as e:
            logger.error(f"{e}")
        



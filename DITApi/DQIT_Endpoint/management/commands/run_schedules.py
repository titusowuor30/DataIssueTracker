from django.core.management.base import BaseCommand
from DQIT_Endpoint.utils import DataImporter  # Import your DataImporter class
from DQIT_Endpoint.models import DataSyncSettings
from DQITAuth.models import BackupSchedule
from django.utils import timezone
from datetime import datetime, time, timedelta
import subprocess
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Import data from Excel and CSV files in a folder using DataImporter according to schedule'

    def handle(self, *args, **options):
        current_time  = datetime.now()
        day_of_week = current_time .strftime('%a').lower()
        time_of_day = current_time .strftime('%H:%M:%S')
        #run data sync
        self.run_datasync(current_time,day_of_week,time_of_day)
        # run backup
        self.run_backup_database(current_time)

    def run_datasync(self,current_time,day_of_week,time_of_day):
        try:
            # Get active backup schedules for the current day and time
            next_run_schedule  = DataSyncSettings.objects.filter(
                day_of_week=day_of_week,
                time_of_day__lte=time_of_day,
                is_active=True
            ).order_by('time_of_day').first()

            if next_run_schedule:
                print(f"Data sync will run on {next_run_schedule.day_of_week} at {next_run_schedule.time_of_day} +2min")
                # Assuming scheduled_time is a datetime.time object
                scheduled_time =next_run_schedule.time_of_day  # Replace with your scheduled time

                # Convert the scheduled_time to a datetime.datetime object
                scheduled_datetime = datetime.combine(datetime.today(), scheduled_time)

                # Add a timedelta of 5 minutes
                scheduled_time_plus_2min = scheduled_datetime + timedelta(minutes=2)

                if current_time >= scheduled_datetime and current_time <= scheduled_time_plus_2min:
                    print("Data sync active...")
                    sync_setup=DataSyncSettings.objects.first()
                    data_importer = DataImporter(sync_setup.data_issues_folder_url)
                    # Run the data importer periodically (e.g., every 1 min)
                    data_importer.check_for_new_files(facility_file_path=sync_setup.faclity_list_csv_path)
            else:
                print(f"No data sync shedule found on {day_of_week} at {time_of_day}")
        except Exception as e:
            print(e)


    def run_backup_database(self,current_time):
        #try:
           schedule = BackupSchedule.objects.first()

           if not schedule.enabled:
                print('Backup schedule is disabled.')
                return

          # Calculate the time difference between now and the next scheduled run
           time_difference = (timezone.make_naive(schedule.next_run_datetime) - current_time).total_seconds()

           if time_difference > 1:
                print(f'Backup schedule will run on {timezone.make_naive(schedule.next_run_datetime)} {time_difference} seconds till then.')
                return

           # Database settings
           db_settings = settings.DATABASES['default']
           #print(db_settings)

           # MySQL database credentials
           db_user = db_settings['USER']
           db_password = db_settings['PASSWORD']
           db_name = db_settings['NAME']

           # Get the task type (backup or restore)
           task_type = schedule.task_type

            # Set the path for the backup file
           backup_dir = os.path.join(os.getcwd(), 'backups')  # Change this path to your desired backup directory
           if not os.path.exists(schedule.folder_path):
                os.makedirs(backup_dir)

           current_datetime = timezone.now()
           backup_file_name = f"{task_type}_{current_datetime.strftime('%Y_%m_%d_%H-%M-%S')}.sql"
           backup_file_path = os.path.join(backup_dir, backup_file_name)

            # Construct the mysqldump command
           mysqldump_cmd = fr"{schedule.mysql_cmd_path} -u{db_user} -p{db_password} -B {db_name} > {backup_file_path}"

           # Execute the mysqldump command
           subprocess.run(mysqldump_cmd, shell=True)

           # Update the last_run_datetime and next_run_datetime in the schedule
           schedule.last_run_datetime = current_datetime
           if schedule.schedule_type == 'daily':
                schedule.next_run_datetime += timezone.timedelta(days=1)
           elif schedule.schedule_type == 'weekly':
                schedule.next_run_datetime += timezone.timedelta(weeks=1)
           elif schedule.schedule_type == 'monthly':
                schedule.next_run_datetime += timezone.timedelta(days=30)  # Approximate for a month
           schedule.save()

        # except BackupSchedule.DoesNotExist:
        #     print('Backup schedule not found.')
        # except subprocess.CalledProcessError as e:
        #     print(f'Error during backup: {e}')
        # except Exception as e:
        #     print(f'Error: {e}')


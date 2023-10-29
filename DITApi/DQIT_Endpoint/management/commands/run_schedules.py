from django.core.management.base import BaseCommand
from DQIT_Endpoint.utils import DataImporter  # Import your DataImporter class
from DQIT_Endpoint.models import DataSyncSettings
from DQITAuth.models import BackupSchedule
from django.utils import timezone
from datetime import datetime, time, timedelta
import subprocess
from django.conf import settings
import os
import threading
import logging
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Import data from Excel and CSV files in a folder using DataImporter according to schedule'

    def handle(self, *args, **options):
        current_time  = datetime.now()
        day_of_week = current_time .strftime('%a').lower()
        time_of_day = current_time .strftime('%H:%M:%S')
        #database credentials
        db_settings = settings.DATABASES['default']
        db_user = db_settings['USER']
        db_password = db_settings['PASSWORD']
        db_name = db_settings['NAME']
        db_host=db_settings['HOST']
        db_port=db_settings['PORT']
        #run data sync
        self.run_datasync(current_time,day_of_week,time_of_day)
        # run backup
        self.run_backup_database(current_time,db_user,db_password,db_name,db_host,db_port)
        # run restore
        self.run_restore_schedule(current_time,db_user,db_password,db_name,db_host,db_port)

    def run_datasync(self,current_time,day_of_week,time_of_day):
        try:
            # for thread in threading.enumerate():
            #     print("Thread Name: {}".format(thread.name),"ID: {}".format(thread.ident),"Is Daemon: {}".format(thread.daemon),"Thread Is Alive: {}".format(thread.is_alive()))
            #     print("Thread Is Current Thread: {}".format(thread == threading.current_thread()))
            #     print()
            # Get active backup schedules for the current day and time
            next_run_schedule  = DataSyncSettings.objects.filter(
                day_of_week=day_of_week,
                time_of_day__lte=time_of_day,
                is_active=True
            ).order_by('time_of_day').first()

            if next_run_schedule:
                logger.info(f"Data sync will run on {next_run_schedule.day_of_week} at {next_run_schedule.time_of_day} +1hr(s)")
                # Assuming scheduled_time is a datetime.time object
                scheduled_time =next_run_schedule.time_of_day  # Replace with your scheduled time

                # Convert the scheduled_time to a datetime.datetime object
                scheduled_datetime = datetime.combine(datetime.today(), scheduled_time)

                # Add a timedelta of 5 minutes
                scheduled_time_plus_1hrs = scheduled_datetime + timedelta(hours=1)

                if current_time >= scheduled_datetime and current_time <= scheduled_time_plus_1hrs:
                    logger.info("Data sync active...")
                    data_importer = DataImporter(next_run_schedule.data_issues_folder_url)
                    data_importer.check_for_new_files(facility_file_path=next_run_schedule.faclity_list_csv_path)
            else:
                logger.error(f"No data sync shedule found on {day_of_week} at {time_of_day}")
        except Exception as e:
            logger.error(e)

    def run_backup_database(self,current_time,db_user,db_password,db_name,db_host,db_port):
        try:
            schedule = BackupSchedule.objects.filter(task_type='backup',enabled=True).first()

            if not schedule.enabled:
                    logger.info('No active schedules found.')
                    return
           
            ########################Backup database######################################
            # Calculate the time difference between now and the next scheduled run
            time_difference = (timezone.make_naive(schedule.next_run_datetime) - current_time).total_seconds()/3600
            logger.info(time_difference)
            if abs(time_difference) >1:
                logger.info(f"Backup schedule will run on {timezone.make_naive(schedule.next_run_datetime)}")
                return
            logger.info("Backing up database...")

            # Get the task type (backup or restore)
            task_type = schedule.task_type

                # Set the path for the backup file
            backup_dir = os.path.join(os.getcwd(), 'backups') #Change this path to your desired backup directory
            if not os.path.exists(backup_dir):
                    os.makedirs(backup_dir)

            current_datetime = timezone.now()
            backup_file_name = f"{task_type}_{current_datetime.strftime('%Y_%m_%d_%H-%M-%S')}.sql"
            backup_file_path = os.path.join(backup_dir, backup_file_name)

            if schedule.db_type=='mysql':
                # Construct the mysqldump command
                mysqldump_cmd = ['mysqldump',f'--host={db_host}',f'--port={db_port}',f'--user={db_user}',f'--password={db_password}',db_name]
                # Run the mysqldump command
                try:
                    with open(backup_file_path, 'w') as backup_file:
                        subprocess.check_call(mysqldump_cmd, stdout=backup_file)
                    self.stdout.write(self.style.SUCCESS(f'Successfully backed up database to {backup_file_path}'))
                except subprocess.CalledProcessError:
                    self.stderr.write(self.style.ERROR('Failed to create a database backup'))
            elif schedule.db_type == 'psql':
                os.environ['PGPASSWORD'] = db_password#set the password
                # Construct the psql dump command
                psql_dump_cmd = ['pg_dump',f'--host={db_host}',f'--port={db_port}',f'--dbname={db_name}',f'--username={db_user}',f'--file={backup_file_path}',]
                # Run the pg_dump command
                try:
                    subprocess.check_call(psql_dump_cmd)
                    self.stdout.write(self.style.SUCCESS(f'Successfully backed up database to {backup_file_path}'))
                except subprocess.CalledProcessError:
                    self.stderr.write(self.style.ERROR('Failed to create a database backup'))
                os.environ.pop('PGPASSWORD', None)#remove the password
                    # Update the last_run_datetime and next_run_datetime in the schedule
                schedule.last_run_datetime = current_datetime
                schedule.start_datetime=current_datetime
                schedule.save()
            else:
                logger.warning("Unknown database")
        except Exception as e:
            logger.error(f'Error: {e}')

    def run_restore_schedule(self,current_time,db_user,db_password,db_name,db_host,db_port):
        try:
            schedule = BackupSchedule.objects.filter(task_type='restore',enabled=True).first()
            current_datetime = timezone.now()
            #restore dir
            restore_dir = os.path.join(os.getcwd(), 'backups')
            #restore file
            restore_file=os.path.join(restore_dir, schedule.restore_file)

            if not schedule.enabled:
                    logger.info('No active schedules found.')
                    return
            
            #####################Restore database############################
            # Calculate the time difference between now and the next scheduled run
            time_difference = (timezone.make_naive(schedule.next_run_datetime) - current_time).total_seconds()/3600 # in hrs
            logger.info(time_difference)
            if abs(time_difference) >1:
                logger.info(f"Restore schedule will run on {timezone.make_naive(schedule.next_run_datetime)}")
                return
            logger.info("Restore in progress...")
            #restore db
            if schedule.db_type=='psql':
                restore_cmd=['psql',f'--host={db_host}',f'--port={db_port}',f'--dbname={db_name}',f'--username={db_user}',f'--file={restore_file}']
                os.environ['PGPASSWORD'] = db_password#set the password
                # Run the psql command
                try:
                    subprocess.check_call(restore_cmd)
                    self.stdout.write(self.style.SUCCESS(f'Successfully restored database file {schedule.restore_file}'))
                except subprocess.CalledProcessError:
                    self.stderr.write(self.style.ERROR(f'Failed to resore database {db_name}'))
                os.environ.pop('PGPASSWORD', None)#remove the password
            elif schedule.db_type == 'mysql':
                pass
            # Update the last_run_datetime and next_run_datetime in the schedule
            schedule.last_run_datetime = current_datetime
            schedule.start_datetime=current_datetime
            schedule.save()
        except Exception as e:
            logger.error(f'Error: {e}')
from apscheduler.schedulers.background import BackgroundScheduler

import os
from shutil import copyfile
import datetime
from django.conf import settings

def job_function():
    print("Hello world")

def database_backup():
    print("Backup data")
    dir_data=os.path.join(settings.BASE_DIR,'Backup')
    currentDT=datetime.datetime.now()
    get_date=str(currentDT.year) + '-' + str(currentDT.month) + '-' + str(currentDT.day)
    file_name = f"{get_date}-{currentDT.minute}-database.sqlite3"
    if not os.path.exists(dir_data):
        os.mkdir(dir_data)
    copyfile(os.path.join(settings.BASE_DIR, 'db.sqlite3'), f"{dir_data}/{file_name}")
    print("Getting Backup is  Successfull")

sched = BackgroundScheduler()

sched.add_job(job_function, 'interval', minutes=1)
sched.add_job(database_backup, 'cron',  hour=20, minute=44)
sched.start()
from datetime import date
import datetime
import os
import shutil

desktop_path = 'C:\\Users\kschwartz\Desktop'
GSCDB_folder_path = "C:\\Users\kschwartz\Desktop\GSCD"
batch_names = []
weekday = datetime.datetime.today().weekday()

if weekday == 0:
    weekday == monday

for i in range(1,6):
    batchnameI = "_batch_" + str(i)
    batch_names.append(batchnameI)

def make_todays_folders():
    today_folder_names = []
    today = date.today()
    today = today.strftime('%m-%d-%y')
    for i in batch_names:
        foldernameI = today + i
        today_folder_names.append(foldernameI)
    print(today_folder_names)
    for i in today_folder_names:
        os.mkdir(os.path.join(desktop_path,i))

def move_yesterdays_folders():
    yesterday_folder_names = []
    yesterday = date.today() - datetime.timedelta(days=1)
    yesteday = yesterday.strftime('%m-%d-%y')
    for i in batch_names:
        foldernameI = str(yesterday) + i
        yesterday_folder_names.append(foldernameI)
    for i in yesterday_folder_names:
        original = os.path.join(desktop_path,i)
        target = os.path.join(GSCDB_folder_path, i)
        shutil.move(original, target)

def move_fridays_folders():
    fri_folder_names = []
    fri = date.today() - datetime.timedelta(days=3)
    fri = fri.strftime('%m-%d-%y')
    for i in batch_names:
        foldernameI = str(fri) + i
        fri_folder_names.append(foldernameI)
    for i in fri_folder_names:
        original= os.path.join(desktop_path,i)
        target = os.path.join(GSCDB_folder_path,i)
        shutil.move(original, target)

if weekday == 0:
    move_fridays_folders()
else:
    move_yesterdays_folders()
make_todays_folders()
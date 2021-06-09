import os
import shutil
import time

path=input("Enter the folder/file name:- ")
days=int(input("Enter the limit for the days:- "))
seconds = time.time() - (days * 24 * 60 * 60)
path=path + '/'

list_of_files = os.listdir(path)

def file_time(path):
                ctime = os.stat(path).st_ctime
                return ctime

if os.path.exists(path):
                for file in list_of_files:
                                if seconds>=file_time:
                                                os.remove(path+file)
                                                print("Files deleted successfully")
                
                                else:
                                                print("The file was created less days ago than the limit you entered")
else:
                print("The path you entered does not exist")



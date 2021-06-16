import os
import shutil
import time

def main():

    days = 30
    #time.time returns current times in second
    seconds = time.time()-(days*24*60*60)
    path = 'C:\\Users\\lenovo\\Desktop\\Projects\\Folder1'

    listofFile = os.listdir(path)

    print(listofFile)

    if os.path.exists(path):
        for route_folder, fodlers, files in os.walk(path):
            if seconds >= get_file_or_folder_age(route_folder):
                remove_folder(route_folder)
            else:
                for folder in fodlers:
                    folder_path = os.path.join(route_folder, folder)
                    if seconds >= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)

                for file in files:
                    file_path = os.path.join(route_folder, file)
                    if seconds >= get_file_or_folder_age(file_path):
                        remove_file(file_path)
        else:
            if seconds >= get_file_or_folder_age(path):
                remove_file(file_path)
            else:
                print("path not found")

def remove_folder(path):
    if not shutil.rmtree(path):
        print("{path} Removed")
    else:
        print("Enable to Delete {path}")

def remove_file(path):
    if not os.remove(path):
        print("{path} Removed!")
    else:
        print("Enable to Delete {path}")

def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime

main()
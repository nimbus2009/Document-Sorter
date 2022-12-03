#Imports
import shutil
import sys
import os
import time
import watchdog

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#Variables
def_from_dir="C:/Users/HP/Downloads"
def_to_dir="C:/Users/HP/Documents"
def_copy_dir="C:/Users/HP/Documents/Sorted"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

#Input variables
from_dir=str(input("Enter the directory of the files to be sorted-"))
if(from_dir==''):
    from_dir=def_from_dir

to_dir=str(input("Enter the destination of the files to be sorted-"))
if(to_dir==''):
    to_dir=def_to_dir

copy_dir=str(input("Enter the destination of the files to be sorted again-"))
if(copy_dir==''):
    copy_dir=def_copy_dir


if(os.path.exists(copy_dir)==False):
    os.mkdir(copy_dir)

path=from_dir
dest=copy_dir

list_of_files=os.listdir(from_dir)

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        name,ext=os.path.splitext(event.src_path)

        for i in dir_tree:
            for j in dir_tree[i]:
                if(ext==j):
                    file_name=os.path.basename(event.src_path)
                    #Prints the tail part of file path
                    print(file_name)

                    key = i

                    print("Downloaded " + file_name)
                    path1 = path + '/' + file_name
                    path2 = dest + '/' + key
                    path3 = dest + '/' + key + '/' + file_name

                    time.sleep(3)

                    if os.path.exists(path2):
                        print("Directory Exists...")
                        print("Moving " + file_name + "....")
                        shutil.move(path1, path3)
                        time.sleep(1)
                    else:
                        print("Making Directory...")
                        os.makedirs(path2)
                        print("Moving " + file_name + "....")
                        shutil.move(path1, path3)
                        time.sleep(1)

                    break


#Initialise the event handler class
event_handler=FileMovementHandler()

#Initialise observer class
observer=Observer()

#Schedule the observer
#The schedule method monitors the specified path which triggers any event to call event_handler
observer.schedule(event_handler,path,recursive=True)
#Start the observer
observer.start()

while True:
    time.sleep(2)
    print("Running...")
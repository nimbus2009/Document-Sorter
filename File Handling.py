import shutil
import os

from_dir="C:/Users/HP/Downloads"
to_dir="C:/Users/HP/Documents"
copy_dir="C:/Users/HP/Documents/Sorted"

list_of_files=os.listdir(from_dir)

if(os.path.exists(copy_dir)==False):
    os.mkdir(copy_dir)

for i in list_of_files:
    name,ext=os.path.splitext(i)
    print(name,ext)
    
    if(ext==''):
        continue
        #-----
    elif(ext=='.png' or ext=='.jpg' or ext=='.gif' or ext=='.jfif' or ext=='.bmp' or ext=='.jpeg'):
        tcd="C:/Users/HP/Documents/Sorted/image_files"

        if(os.path.exists(tcd)==False):
            os.mkdir(tcd)

        imageToBeCopied=from_dir+'/'+str(i)
        shutil.copy(imageToBeCopied,tcd)
        #-----
    elif(ext=='.ppt' or ext=='.xls' or ext=='.xlsx' or ext=='.csv' or ext=='.pdf' or ext=='.txt'):
        tcd="C:/Users/HP/Documents/Sorted/office_files"

        if(os.path.exists(tcd)==False):
            os.mkdir(tcd)
        
        fileToBeCopied=from_dir+'/'+str(i)
        shutil.copy(fileToBeCopied,tcd)
        #----- 
        
    elif(ext=='.exe' or ext=='.bin' or ext=='.cmd' or ext=='.msi' or ext=='.dmg'):
        tcd="C:/Users/HP/Documents/Sorted/setup_files"

        if(os.path.exists(tcd)==False):
            os.mkdir(tcd)
        
        fileToBeCopied=from_dir+'/'+str(i)
        shutil.copy(fileToBeCopied,tcd)
        #-----

    elif(ext=='.mpg' or ext=='.mp2' or ext=='.mpeg' or ext=='.mpe' or ext=='.mpv' or ext=='.mp4' or ext=='.avi' or ext=='.mov'):
        tcd="C:/Users/HP/Documents/Sorted/video_files"

        if(os.path.exists(tcd)==False):
            os.mkdir(tcd)
        
        videoToBeCopied=from_dir+'/'+str(i)
        shutil.copy(videoToBeCopied,tcd)
        
    elif():
        if(ext=='' or ext==' '):
            continue
        else:
            tcd="C:/Users/HP/Documents/Sorted/other_files"

            if(os.path.exists(tcd)==False):
                os.mkdir(tcd)
            
            fileToBeCopied=from_dir+'/'+str(i)
            shutil.copy(fileToBeCopied,tcd)

            continue

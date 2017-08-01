
# Created By Jake Stephens


import os
import datetime
import shutil



def runReport(currentPath, targetPath, targetDate):

    if not os.path.isdir("Reports"):
        os.makedirs("Reports")

    # Open Report   
    name = "Reports/temp.txt"
    report = open(name, 'w')


    # running count of total files moved
    count = 0
    # iterate through all directories in currentPath
    for dirPath, dirs, files in os.walk('.\\'+currentPath): 

        # iterate through all files in all directories in currentPath
        for item in os.listdir(dirPath):
            # update file path
            filePath = dirPath+'\\'+item

            # if it is a file
            if os.path.isfile(filePath):
                # get date last modified
                t = os.path.getmtime(filePath)
                modDate  = str(datetime.datetime.fromtimestamp(t))
                modYear  = int(modDate[0:4])
                modMonth = int(modDate[5:7])
                modDay   = int(modDate[8:10])
                modDate  = datetime.date(modYear, modMonth, modDay).isoformat()

                # if date last modified was longer than specified date
                if modDate < targetDate:
                    # increment counter
                    count+=1
                    # Add to report
                    report.write(filePath+"\n")


    # total files moved
    report.write("Number of Files: "+str(count))

    # Close Report
    report.close()

    return (name)




def rename(newPath2):
    count = 1
    newPath3 = newPath2
    while os.path.isfile(newPath3):
        new = '('+str(count)+')'
        newPath3 = newPath2+new
        count+=1
    return newPath3




def archive(currentPath, targetPath, targetDate):

    if not os.path.isdir("Reports"):
        os.makedirs("Reports")

    # Open Report
    currentDate  = str(datetime.datetime.now())

    splitDate = currentDate.split("-")
    splitDay  = splitDate[2].split(" ")
    splitTime = splitDay[1].split(":")
    splitSec  = splitTime[2].split(".")

    name = "Reports/"+splitDate[1]+"-"+splitDay[0]+"-"+splitDate[0]+"--"+splitTime[0]+"-"+splitTime[1]+"-"+splitSec[0]+".txt"
    report = open(name, 'w')


    # running count of total files moved
    count = 0
    # iterate through all directories in currentPath
    for dirPath, dirs, files in os.walk('.\\'+currentPath): 
        # updates path
        split = dirPath.split('\\')
        split[1] = targetPath
        newPath = '\\'.join(split)
    
        # if the directory does not exist in archives then add it
        if not os.path.isdir(newPath):
            os.makedirs(newPath)

        # iterate through all files in all directories in currentPath
        for item in os.listdir(dirPath):
            # update file path
            filePath = dirPath+'\\'+item

            # if it is a file
            if os.path.isfile(filePath):
                # get date last modified
                t = os.path.getmtime(filePath)
                modDate  = str(datetime.datetime.fromtimestamp(t))
                modYear  = int(modDate[0:4])
                modMonth = int(modDate[5:7])
                modDay   = int(modDate[8:10])
                modDate  = datetime.date(modYear, modMonth, modDay).isoformat()

                # if date last modified was longer than specified date
                if modDate < targetDate:
                    # increment counter
                    count+=1
                    # Add to report
                    report.write(filePath+"\n")

                    # Formats the Archive Path
                    split2 = filePath.split('\\')
                    split2[1] = targetPath
                    newPath2 = '\\'.join(split2)

                    # if the file name is already used in archives, add (1)
                    if os.path.isfile(newPath2):
                        newPath2 = rename(newPath2)

                    # move file to archive directory
                    shutil.move(filePath, newPath2)


    # total files moved
    report.write("Number of Files Moved: "+str(count))

    # Close Report
    report.close()

    return (name)



def clearTempFiles():
    # for item in os.listdir("temp"):
    #     os.remove("temp/"+item)
    if os.path.isfile("Reports/temp.txt"):
        os.remove("Reports/temp.txt")
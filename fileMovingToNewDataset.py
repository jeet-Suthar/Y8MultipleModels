# second step

# this script will move all necessary data to new directory which will have data in order
# it will move only those files which were rename in previous script
# all rest are not copied in new directory
# hope this program will be easy to understand
# Good luck!


import os
import shutil
import re
from pathlib import Path


def sorted_alphanumeric(data):  # function for arrangung names in order
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(data, key=alphanum_key)


rootDir = "D:\\Jeet's folder\\Code\\projects\\bhishma\\Train data\\edit test\\same name rename"
movingDir = "D:\\Jeet's folder\\Code\\projects\\bhishma\\Train data\\unassembled data"

MultipleDatasets = ["knife train data", 'fire_smoke train data', 'tank train data','Pistol train data']
YolosubDir = ['test', 'train', 'valid']     # this will remain unchanged

for dataSets_ in MultipleDatasets:      # for every dataset
    print("\n\nWe are performing data manuplation on " + dataSets_)
    os.chdir(movingDir)     # will always return directory to moving folder IT IS IMP

    desDir = movingDir + '\\' + dataSets_  # assigning path in one variable
    Path(desDir).mkdir(exist_ok=True)       # it will make directory of corresponding dir name inside moving dir
    newMovingDir = movingDir + '\\' + dataSets_

    for Subdir_ in YolosubDir:  # for three subdirectory in dataset i.e test train valid

        srcDir = rootDir + '\\' + dataSets_ + '\\' + Subdir_  # source path from which data is to be copied

        desDir = newMovingDir + '\\' + Subdir_  # assigning path of destination
        Path(desDir).mkdir(exist_ok=True)       # it will make subdir inside particular data

        # for images

        Path(desDir + '\\' + "images").mkdir(exist_ok=True)  # it will make images folder inside subdirectory

        # hereby we have created directory [dataset] inside and create further directory as per YOLO requirements
        # i.e. movingDir\\dataset\\SubDir\\images
        # for e.g. rename\\tank train data\\test\\images

        sortedlst = sorted_alphanumeric(os.listdir(srcDir + '\\' + "images"))  # getting sorted list of files
        print("No. of images and annotation in " + srcDir + " are " + str(len(sortedlst)))  # display no files in directory

        print('\n'*5,'Images','\n'*5,)

        # for each image in current dir
        for file in sortedlst:  # for every file current dir
            if file == ".DS_Store":
                continue
            stemName, ext = os.path.splitext(file)

            if (stemName[3] == '_'):
                os.chdir(srcDir + '\\' + 'images')  # changing dir for copying files ITS MANDATORY
                shutil.copy(file, desDir + '\\' + 'images')
                print(file)

        # for annotations (labels)

        print('\n'*5,'labels','\n'*5,)


        Path(desDir + '\\' + "labels").mkdir(exist_ok=True)     # for making labels folder inside subdirectory

        sortedlst = sorted_alphanumeric(os.listdir(srcDir + '\\' + "labels"))   # getting sorted list of files

        for file in sortedlst:  # for every file current dir
            if file == ".DS_Store":
                continue
            stemName, ext = os.path.splitext(file)

            if (stemName[3] == '_'):
                os.chdir(srcDir + '\\' + 'labels')  # changing dir for copying files ITS MANDATORY
                shutil.copy(file, desDir + '\\' + 'labels')
                print(file)



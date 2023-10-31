# fourth step and final step


import os
import shutil
import re
from pathlib import Path


def sorted_alphanumeric(data):  # function for arrangung names in order
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(data, key=alphanum_key)


rootDir = "D:\\Jeet's folder\\Code\\projects\\bhishma\\Train data\\unassembled data"
FinalDir = "D:\\Jeet's folder\\Code\\projects\\bhishma\\Train data\\bhishma_V1.0"

MultipleDatasets = ["knife train data", 'fire_smoke train data', 'tank train data','Pistol train data']
YolosubDir = ['test', 'train', 'valid']     # this will remain unchanged

for dataSets_ in MultipleDatasets:
    os.chdir(FinalDir)     # will always return directory to moving folder IT IS IMP

    for Subdir_ in YolosubDir:

        srcDir = rootDir + '\\' + dataSets_ + '\\' + Subdir_  # source path from which data is to be copied
        desDir = FinalDir + '\\' + Subdir_
        Path(desDir).mkdir(exist_ok=True)

        Path(desDir + '\\' + "images").mkdir(exist_ok=True)  # it will make images folder inside subdirectory

        sortedlst = sorted_alphanumeric(os.listdir(srcDir + '\\' + "images"))    # getting sorted list of files

        print('\n'*5,'Images','\n'*5,)

        for file in sortedlst:  # for every file current dir
            if file == ".DS_Store":
                continue
            os.chdir(srcDir + '\\' + 'images')  # changing dir for copying files ITS MANDATORY
            shutil.copy(file, desDir + '\\' + 'images')
            print(file)

        print('\n'*5,'labels','\n'*5,)

        Path(desDir + '\\' + "labels").mkdir(exist_ok=True)     # for making labels folder inside subdirectory

        sortedlst = sorted_alphanumeric(os.listdir(srcDir + '\\' + "labels"))  # getting sorted list of files

        for file in sortedlst:  # for every file current dir
            if file == ".DS_Store":
                continue
            os.chdir(srcDir + '\\' + 'labels')  # changing dir for copying files ITS MANDATORY
            shutil.copy(file, desDir + '\\' + 'labels')
            print(file)



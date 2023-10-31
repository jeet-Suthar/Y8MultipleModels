# First step

# program for changing name of images and annotation files into proper format.
# here name will convert from img(1).jpg into img_00001.jpg for selected count of files
# that means if you want 150 images from test images of dataset_1 then this program will rename those many only
# rest all images and labels will be remained in format img(10.jpg or img(1).txt

import os
import shutil
import re
from pathlib import Path

def sorted_alphanumeric(data):              # function for arrangung names in order
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(data, key=alphanum_key)

rootDir = "D:\\Jeet's folder\\Code\\projects\\bhishma\\Train data\\edit test\\same name rename"

print(os.getcwd())

MultipleDatasets = ["knife train data",'fire_smoke train data','tank train data','Pistol train data']
YolosubDir = ['test','train','valid']

data = [[50,100,150,50],[500,2000,1000,700],[100,150,150,150]]
countDict = dict(zip(YolosubDir, data))
# print(dictionary['test'])

currentCountData = [0,0,0]
currentCountDict = dict(zip(YolosubDir,currentCountData))       # count for images

currentCountAnnotation = [0,0,0]
currentCountDictAnnotation = dict(zip(YolosubDir,currentCountAnnotation))   # count for annotation

GlobalDataCount=[]      # total no. of images
for j in countDict:
    eachTotal = 0
    for i in countDict[j]:
        eachTotal += i
    GlobalDataCount.append(eachTotal)

print('total count will be :\ntest =>',GlobalDataCount[0],'\ntrain =>',GlobalDataCount[1],'\nvalid =>',GlobalDataCount[2],)


for dataSets_ in MultipleDatasets:      # for every data
    print("\n\nWe are performing data manipulation on "+dataSets_)

    for Subdir_ in YolosubDir:      # for three subdirectory in dataset i.e test train valid


        cwd= rootDir + '\\' + dataSets_ + '\\' + Subdir_        # assigning path in one variable
        print(cwd)     # will print current dir which we are currently working on

        sortedlst = sorted_alphanumeric(os.listdir(cwd + '\\'+ "images"))       # gets sorted list
        print("No. of images in "+cwd+" are "+str(len(sortedlst)))

        # for each image in current dir
        os.chdir(cwd + "\\images")          # will change dir to images as it NECESSARY for renaming

        for file in sortedlst:
            if sortedlst.index(file) < countDict[Subdir_][MultipleDatasets.index(dataSets_)]:  # checking count
                currentCountDict[Subdir_] += 1      # incrementing variable which keeping count of files

                stemName, ext = os.path.splitext(file)      # will spilt stem name and extension

                newStemName = f'img_{currentCountDict[Subdir_]:05d}{ext}'       # will assign new name to current file
                os.rename(file,newStemName)                                   # will rename file
                print(newStemName)
                print(currentCountDict[Subdir_])


        sortedlst = sorted_alphanumeric(os.listdir(cwd + '\\' + "labels"))
        print("No. of labels in " + cwd + " are " + str(len(sortedlst)))

        # for each labels in current dir
        os.chdir(cwd + "\\labels")      # will change dir to labels as it NECESSARY for renaming

        for file in sortedlst:  # for every file current dir
            if sortedlst.index(file) < countDict[Subdir_][MultipleDatasets.index(dataSets_)]:  # checking count
                currentCountDictAnnotation[Subdir_] += 1  # incrementing variable which keeping count of files

                stemName, ext = os.path.splitext(file)  # will spilt stem name and extension

                newStemName = f'img_{currentCountDictAnnotation[Subdir_]:05d}{ext}'  # will assign values from current count
                os.rename(file,newStemName)                                   # will rename file
                print(newStemName)
                print(currentCountDictAnnotation[Subdir_])

print('total count will be :\ntest =>',GlobalDataCount[0],'\ntrain =>',GlobalDataCount[1],'\nvalid =>',GlobalDataCount[2],)
print("\n\nTotal imags :",GlobalDataCount[0]+GlobalDataCount[1]+GlobalDataCount[2])
print("\n\nTotal files (include images and labels): ",(GlobalDataCount[0]+GlobalDataCount[1]+GlobalDataCount[2])*2)







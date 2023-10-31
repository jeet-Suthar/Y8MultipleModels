# third step
# here main process that is changing class id will be accomplished



import os
import re

def sorted_alphanumeric(data):  # function for arrangung names in order
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(data, key=alphanum_key)


oldClassId = [0,1,2,3,4]
newClassId = [2,6,0,7,1]



datasetDir = "D:\\Jeet's folder\\Code\\projects\\bhishma\\Train data\\unassembled data\\fire_smoke train data"
YolosubDir = ['test', 'train', 'valid']     # this will remain unchanged


for Subdir_ in YolosubDir:
    cwd = datasetDir + "\\" + Subdir_

    sortedlst = sorted_alphanumeric(os.listdir(cwd  + '\\' + "labelss"))  # gets sorted list
    print("No. of images and annotation in " + cwd + " are " + str(len(sortedlst)))  # display no files in directory

    for file in sortedlst:
        Lines = []
        print('\n'*3,file)
        with open(cwd + '\\' + "labelss" + '\\' + file, "r") as r:
            for line in r.readlines():
                Lines.append(line)  # will append annotations to list Lines[]

        print("Lines", Lines)


        newLines = []

        for eachLine in Lines:  # for loop for each index of Lines[] list
            for j in range(len(newClassId)):  # for loop for each element in newClassID
                if (eachLine[0] == str(oldClassId[j])):  # checking first element of string eachLine to oldClassID
                    newEachLine = str(newClassId[j]) + eachLine[1:]  # if matches then replace with corresponding ID in newClassID
                    newLines.append(newEachLine)  # appending newly created string to newDataset
        print("\n\nnew lines", newLines)

        with open(cwd + '\\'+ "labels" + '\\' + file, "w") as w:
            for updatedLine in range(len(newLines)):
                w.write(newLines[updatedLine])
    print("\n\n\nsuccessfully updated")






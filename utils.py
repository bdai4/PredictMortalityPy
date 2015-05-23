# -*- coding: utf-8 -*-

def readData():
    dataFile = open("files_input.txt", 'r').read().splitlines()

    PatientsList = list()
    for current_file in (dataFile):
        with open(current_file) as f:
            PatientsList.append(f.readlines())

    return PatientsList;

listTest = readData()
print(len(listTest))
print(listTest[0])

# -*- coding: utf-8 -*-

def readData():
    dataFile = open("files_input.txt", 'r').read().splitlines()

    PatientsList = list()
    for current_file in (dataFile):
        f = open(current_file, 'r').read().splitlines()
        f[0] = f[0].split(',')
        PatientsList.append(f)

    return PatientsList;

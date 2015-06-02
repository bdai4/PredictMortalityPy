# -*- coding: utf-8 -*-


def readData():
    dataFile = open("files_input.txt", 'r').read().splitlines()

    patientsList = list()
    for current_file in (dataFile):
        patient = {'Time': list(), 'Parameter': list(), 'Value': list()}

        f = open(current_file, 'r').read().splitlines()
        for index, value in enumerate(f):
            if index != 0:
                temp = f[index].split(',')
                patient["Time"].append(convertTime(temp[0]))
                patient["Parameter"].append(temp[1])
                patient["Value"].append(temp[2])
        patientsList.append(patient)

    return patientsList


def convertTime(temp):
    hour, minutes = temp.split(':')
    return int((hour * 60) + minutes)

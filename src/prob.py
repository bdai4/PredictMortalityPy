# -*- coding: utf-8 -*-

import utils
import saps_score

patientList = utils.readData()
scoreList = list()
for patient in xrange(0, len(patientList)):
    scoreList.append(saps_score.saps_score(patientList[patient]))


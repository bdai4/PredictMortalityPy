# -*- coding: utf-8 -*-

MISSING = (-2)
INVALID = (-1)


def saps_score(data):
    missing = 0
    urine_tot = 0.

    s_age = s_hr = s_sbp = s_temp = s_resp = s_ur = s_bun = MISSING
    s_hct = s_wbc = s_glu = s_k = s_na = s_hco3 = s_gcs = MISSING

    def Age(value):
        s_age = (score_age(value)) > s_age

    def HR(value):
        s_hr = (score_hr(value)) > s_hr

    def SysABP(value):
        s_sbp = (score_sbp(value)) > s_sbp

    def NISysABP(value):
        s_sbp = (score_sbp(value)) > s_sbp

    def Temp(value):
        s_temp = (score_temp(value)) > s_temp

    def RespRate(value):
        s_resp = (score_resp(value)) > s_resp

    def MechVent(value):
        s_resp = (score_resp(value)) > s_resp

    def Urine(value):
        urine_tot += float(value)

    def BUN(value):
        s_bun = (score_bun(float(value))/2.8) > s_bun

    def HCT(value):
        s_hct = (score_hct(value)) > s_hct

    def WBC(value):
        s_wbc = (score_wbc(value)) > s_wbc

    def Glucose(value):
        s_glu = (score_glu(value)) > s_glu

    def K(value):
        s_k = (score_k(value)) > s_k

    def Na(value):
        s_na = (score_na(value)) > s_na

    def HCO3(value):
        s_hco3 = (score_hco3(value)) > s_hco3

    def GCS(value):
        s_gcs = (score_gcs(value)) > s_gcs

    parameters = {"Age": Age, "HR": HR, "SysABP": SysABP, "NISysABP": NISysABP,
                  "Temp": Temp, "RespRate": RespRate, "MechVent": MechVent,
                  "Urine": Urine, "BUN": BUN, "HCT": HCT, "WBC": WBC,
                  "Glucose": Glucose, "K": K, "Na": Na, "HCO3": HCO3, "GCS": GCS}

    # examine data from the first 24 hours only
    for index, element in enumerate(data["Parameter"]):
        if (data["Time"][index] <= 24 * 60):
            if (data["Parameter"][index] in parameters):
                parameters[data["Parameter"][index]](data["Value"][index])

    # s_ur is determined by total urine output over 24 hours
    s_ur = score_ur(urine_tot / 1000.0)
    saps = 0

    # Sum the SAPS components.
    if (s_age):
        saps = 1
    else:
        missing = missing + 1
    if (s_hr):
        saps += s_hr
    else:
        missing = missing + 1
    if (s_sbp):
        saps += s_sbp
    else:
        missing = missing + 1
    if (s_temp):
        saps += s_temp
    else:
        missing = missing + 1
    if (s_resp):
        saps += s_resp
    else:
        missing = missing + 1
    if (s_ur):
        saps += s_ur
    else:
        missing = missing + 1
    if (s_bun):
        saps += s_bun
    else:
        missing = missing + 1
    if (s_hct):
        saps += s_hct
    else:
        missing = missing + 1
    if (s_wbc):
        saps += s_wbc
    else:
        missing = missing + 1
    if (s_glu):
        saps += s_glu
    else:
        missing = missing + 1
    if (s_k):
        saps += s_k
    else:
        missing = missing + 1
    if (s_na):
        saps += s_na
    else:
        missing = missing + 1
    if (s_hco3):
        saps += s_hco3
    else:
        missing = missing + 1
    if (s_gcs):
        saps += s_gcs
    else:
        missing = missing + 1

    if (missing == 0):
        return saps
    else:
        return (-saps)  # return partial scores as negative


def score_age(age):
    if (age > 200):
        return INVALID
    elif (age > 75):
        return 4
    elif (age > 65):
        return 3
    elif (age > 55):
        return 2
    elif (age > 45):
        return 1
    elif (age >= 0):
        return 0
    else:
        return MISSING


def score_hr(hr):
    if (hr > 250):
        return INVALID
    elif (hr >= 180):
        return 4
    elif (hr >= 140):
        return 3
    elif (hr >= 110):
        return 2
    elif (hr >= 70):
        return 0
    elif (hr >= 55):
        return 2
    elif (hr >= 40):
        return 3
    elif (hr >= 10):
        return 4
    elif (hr >= 0):
        return INVALID
    else:
        return MISSING


def score_sbp(sbp):
    if (sbp > 300):
        return INVALID
    elif (sbp >= 190):
        return 4
    elif (sbp >= 150):
        return 2
    elif (sbp >= 80):
        return 0
    elif (sbp >= 55):
        return 2
    elif (sbp >= 20):
        return 4
    elif (sbp >= 0):
        return INVALID
    else:
        return MISSING


def score_temp(temp):
    if (temp > 45):
        return INVALID
    elif (temp >= 41):
        return 4
    elif (temp >= 39):
        return 3
    elif (temp >= 38.5):
        return 2
    elif (temp >= 36):
        return 0
    elif (temp >= 34):
        return 1
    elif (temp >= 32):
        return 2
    elif (temp >= 30):
        return 3
    elif (temp >= 15):
        return 4
    elif (temp >= 0):
        return INVALID
    else:
        return MISSING


def score_resp(resp):
    if (resp > 80):
        return INVALID
    elif (resp >= 50):
        return 4
    elif (resp >= 35):
        return 3
    elif (resp >= 25):
        return 1
    elif (resp >= 12):
        return 0
    elif (resp >= 10):
        return 1
    elif (resp >= 6):
        return 2
    elif (resp >= 2):
        return 4
    elif (resp >= 0):
        return INVALID
    else:
        return MISSING


def score_ur(ur):
    if (ur > 20.0):
        return INVALID
    elif (ur >= 5.0):
        return 2
    elif (ur >= 3.5):
        return 1
    elif (ur >= 0.7):
        return 0
    elif (ur >= 0.5):
        return 2
    elif (ur >= 0.2):
        return 3
    elif (ur >= 0):
        return 4
    else:
        return MISSING


def score_bun(bun):
    if (bun > 100):
        return INVALID
    elif (bun >= 55):
        return 4
    elif (bun >= 36):
        return 3
    elif (bun >= 29):
        return 2
    elif (bun >= 7.5):
        return 1
    elif (bun >= 3.5):
        return 0
    elif (bun >= 1):
        return 1
    elif (bun >= 0):
        return INVALID
    else:
        return MISSING


def score_hct(hct):
    if (hct > 80):
        return INVALID
    elif (hct >= 60):
        return 4
    elif (hct >= 50):
        return 2
    elif (hct >= 46):
        return 1
    elif (hct >= 30):
        return 0
    elif (hct >= 20):
        return 2
    elif (hct >= 5):
        return 4
    elif (hct >= 0):
        return INVALID
    else:
        return MISSING


def score_wbc(wbc):
    if (wbc > 200):
        return INVALID
    elif (wbc >= 40):
        return 4
    elif (wbc >= 20):
        return 2
    elif (wbc >= 15):
        return 1
    elif (wbc >= 3):
        return 0
    elif (wbc >= 1):
        return 2
    elif (wbc >= 0.1):
        return 4
    elif (wbc >= 0):
        return INVALID
    else:
        return MISSING


def score_glu(glu):
    if (glu > 1000):
        return INVALID
    elif (glu >= 44.5):
        return 4
    elif (glu >= 27.8):
        return 3
    elif (glu >= 14.0):
        return 1
    elif (glu >= 3.9):
        return 0
    elif (glu >= 2.8):
        return 2
    elif (glu >= 1.6):
        return 3
    elif (glu >= 0.5):
        return 4
    elif (glu >= 0):
        return INVALID
    else:
        return MISSING


def score_k(k):
    if (k > 20):
        return INVALID
    elif (k >= 7.0):
        return 4
    elif (k >= 6.0):
        return 3
    elif (k >= 5.5):
        return 2
    elif (k >= 3.5):
        return 0
    elif (k >= 3.0):
        return 1
    elif (k >= 2.5):
        return 2
    elif (k >= 0.5):
        return 4
    elif (k >= 0):
        return INVALID
    else:
        return MISSING


def score_na(na):
    if (na > 200):
        return INVALID
    elif (na >= 180):
        return 4
    elif (na >= 161):
        return 3
    elif (na >= 156):
        return 2
    elif (na >= 151):
        return 1
    elif (na >= 130):
        return 0
    elif (na >= 120):
        return 2
    elif (na >= 110):
        return 3
    elif (na >= 50):
        return 4
    elif (na >= 0):
        return INVALID
    else:
        return MISSING


def score_hco3(hco3):
    if (hco3 > 100):
        return INVALID
    elif (hco3 >= 40):
        return 4
    elif (hco3 >= 30):
        return 1
    elif (hco3 >= 20):
        return 0
    elif (hco3 >= 10):
        return 1
    elif (hco3 >= 5):
        return 2
    elif (hco3 >= 2):
        return 4
    elif (hco3 >= 0):
        return INVALID
    else:
        return MISSING


def score_gcs(gcs):
    if (gcs > 15):
        return INVALID
    elif (gcs >= 13):
        return 0
    elif (gcs >= 10):
        return 1
    elif (gcs >= 7):
        return 2
    elif (gcs >= 4):
        return 3
    elif (gcs >= 3):
        return 4
    elif (gcs >= 0):
        return INVALID
    else:
        return MISSING

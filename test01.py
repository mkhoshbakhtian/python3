from math import log

def main_ex():
    THOUT = 40
    THIN = 160
    TCIN = 40
    TCOUT = 180
    U = 0.4
    mcpcold = 40.0
    mcphot = 30.0
    Period = 80000
    Deltamin = 10
    NewTHout = THOUT + Deltamin
    TCOUTcalculated = TCIN + (THIN - NewTHout) * (mcphot / mcpcold)
    DeltaT1 = THIN - TCOUTcalculated
    DeltaT2 = NewTHout - TCIN
    deltalm_EX = (DeltaT1 - DeltaT2) / log(DeltaT1 / DeltaT2)
    Qex = (THIN - NewTHout) * mcphot
    Areaex = Qex / (U * deltalm_EX)
    Cost_EX = 40000 + 180000 * Areaex ** 0.6
    print (DeltaT1)
    print (DeltaT2)
    print (deltalm_EX)
    print (Qex, TCOUTcalculated)
    print (Areaex)
    return round(Cost_EX, 3)


def steam_cost():

    SteamTemp  = 200
    TCOUT = 122.5
    U = 0.4
    mcpcold = 40
    steamcost = 0.1
    Period = 80000
    DeltaT1 = SteamTemp - TCOUT
    DeltaT2 = SteamTemp - 180
    deltalm_EX = (DeltaT1 - DeltaT2) / log(DeltaT1 / DeltaT2)
    Qsteam = (180 - TCOUT) * mcpcold
    Areast = Qsteam / (U * deltalm_EX)
    Cost_st = (Qsteam * steamcost * Period)+ (40000 + 180000 * Areast ** 0.6)
    print (deltalm_EX)
    print (Qsteam)
    print (Areast)
    return round(Cost_st, 3)


def cw_cost():
    CWTemp = 20.0
    THOUT = 40
    U = 0.4
    mcphot = 30
    CWcost = 0.005
    Period = 80000
    Deltamin = 10
    NewTHout = THOUT + Deltamin
    DeltaT2 = THOUT - CWTemp
    DeltaT1 = NewTHout - CWTemp
    ratio = DeltaT1/DeltaT2
    deltalm_EX = (DeltaT1 - DeltaT2) / log(ratio) #(30-20)/log(1.5)
    Qcw = (NewTHout - THOUT ) * mcphot
    Areaex = Qcw / (U * deltalm_EX)
    Cost_CW = (Qcw * CWcost * Period) + (40000 + 180000 * Areaex ** 0.6)
    print (DeltaT1)
    print (DeltaT2)
    print (deltalm_EX)
    print (Qcw)
    print (Areaex)
    return round(Cost_CW, 3)

#print(steam_cost())
print(main_ex())
#print (cw_cost())


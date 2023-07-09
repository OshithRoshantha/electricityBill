def chargeOnUnits(noUnits):
    if noUnits<=60:
        if noUnits<=30:
            return noUnits*10
        else:
            return (noUnits-30)*25+300
    else:
        if noUnits<=60:
            return noUnits*32
        elif noUnits<=90:
            return (noUnits-60)*35+1920
        elif noUnits<=120:
            return (noUnits-90)*50+2970
        elif noUnits<=180:
            return (noUnits-120)*50+4470
        else:
            return (noUnits-180)*75+7470
            
def chargeFixed(noUnits):
    if noUnits<=30:
        return 150
    elif noUnits<=60:
        return 300
    elif noUnits<=90:
        return 400
    elif noUnits<=120:
        return 1000
    elif noUnits<=180:
        return 1500
    else:
        return 2000
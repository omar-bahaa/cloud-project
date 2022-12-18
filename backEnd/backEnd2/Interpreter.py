import json
from ZonesConfig import *

def readInputData(dataFilePath):
    dataFile=open(dataFilePath)
    data = json.load(dataFile)
    return data

"""
{
"ZSs":{
        "Active": str,
        "No_of_ZSs": int,
        "ZoneSets":{
            str:{
                "ZSname": str,
                "mappings": [[str, str], [str, str]],
                "password": str
            }
        }
    }

    }
"""
def getZonesetsConfig(dataFilePath):
    data=readInputData(dataFilePath)
    activeZoneSetName=data["ZSs"]["Active"]
    
    #3ayzen nkhly activeZoneset tb2a instance attribute not class attribute
    ZoneSet.activeZoneset=activeZoneSetName
    ZoneSet.allZoneset.add()
    #totalNumberOfZonesets=data["ZSs"]["No_of_ZSs"]
    zonesets=data["ZSs"]["ZoneSets"]
    for zoneset in zonesets.keys():
        myZoneset=ZoneSet(data["ZSs"]["ZoneSets"]["ZSname"])
        ZoneSet.allZoneset.add(myZoneset)
        for mapping in data["ZSs"]["ZoneSets"]["mappings"]:
            myZoneset.addZoneGroupPairToZoneSet(mapping[0],mapping[1])





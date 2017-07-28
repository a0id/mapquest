import json, hashlib, random, requests
import urllib.request as urllib2
from pprint import pprint



class Map():
    def __init__(self, key):
        self.startLoc = []
        self.key = key
        self.endLoc = []
        self.information = []
        self.data = ""
        self.locData = ""
    def getInfo(self):
        self.information = [
            "Unpaved roads: " + str(self.data["route"]["hasUnpaved"]),
            "Distance (mi.): " + str(self.data["route"]["distance"]),
            "Time (min.): " + str(int(self.data["route"]["time"]/60)),
            "Latitude (dest.): " + str(self.data["route"]["locations"][0]["latLng"]["lat"]),
            "Longitude (dest.): " + str(self.data["route"]["locations"][0]["latLng"]["lng"]),
            "Side of street (dest.): " + str(self.data["route"]["locations"][1]["sideOfStreet"]),
        ]
        print(self.information)
    def traffic(self):
        request = (
            "http://www.mapquestapi.com/traffic/v2/incidents?key=" + self.key + "&boundingBox=" + 
            str(self.data["route"]["locations"][0]["latLng"]["lat"]) + "," + 
            str(self.data["route"]["locations"][0]["latLng"]["lng"]) + "," +  
            str(self.data["route"]["locations"][1]["latLng"]["lat"]) + "," + 
            str(self.data["route"]["locations"][1]["latLng"]["lng"])
            + "&filters=construction,incidents"
        )
        accidents = []
        self.data = requests.get(request).json()
        for x in range(len(self.data["incidents"])):
            accidents.append("Accident " + str(x+1) + ": " + self.data["incidents"][x]["shortDesc"])
        return accidents
    def parse(self, place, arr):
        arr.append(self.locData[place]["address"])
        arr.append(self.locData[place]["city"])
        arr.append(self.locData[place]["state"])
    def newRequest(self):
        with open('location.json') as data_file:
            self.locData = json.load(data_file)
            self.parse("start", self.startLoc)
            self.parse("end", self.endLoc)
        request = (
            "http://www.mapquestapi.com/directions/v2/route?key=" + self.key + 
            "&from=" + self.startLoc[0] + ",+" + self.startLoc[1] + ",+" + self.startLoc[2] + 
            "&to=" + self.endLoc[0] + ",+" + self.endLoc[1] + ",+" + self.endLoc[2]
        )
        self.data = requests.get(request).json()
        with open("temp/currRequest.json", "w") as d:
            json.dump(self.data, d)
loc = Map("9OHwFcxHckgLKLRaCjIkdVr0dXDAqlO9")
loc.newRequest()
print(loc.getInfo())
print(loc.traffic())
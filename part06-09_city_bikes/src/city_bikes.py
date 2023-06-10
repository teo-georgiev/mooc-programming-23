# tee ratkaisu tänne
# Write your solution here
import math

def get_station_data(filename: str): 
    stationData = {}
    with open(filename) as newFile: 
        for line in newFile: 
            line = line.replace("\n", "")
            parts = line.split(";")
            name = parts[3]
            if parts[3] == "name": 
                continue
            stationData[name] = float(parts[0]), float(parts[1] )

    # for key, value in stationData.items(): 
    #     print(f"{key}: ({value[0]}, {value[1]})")
    
    return stationData

def distance(station: dict, station1: str, station2: str): 
    stationCoord1 = station[station1]
    stationCoord2 = station[station2]
    
    x_km = (stationCoord1[0] - stationCoord2[0]) * 55.26
    y_km = (stationCoord1[1] - stationCoord2[1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations: dict): 
    copiedStations = stations.copy()

    greatestDistInfo = ("", "", 0)
    for key1, value1 in stations.items(): 
        for key2, value2 in copiedStations.items(): 
            greatestDist = 0
            if key1 == key2: 
                continue
            stationCoord1 = stations[key1]
            stationCoord2 = copiedStations[key2]

            x_km = (stationCoord1[0] - stationCoord2[0]) * 55.26
            y_km = (stationCoord1[1] - stationCoord2[1]) * 111.2
            distance_km = math.sqrt(x_km**2 + y_km**2)
            if distance_km > greatestDist: 
                greatestDist = distance_km
                name1 = key1
                name2 = key2

            if greatestDist > float(greatestDistInfo[2]): 
                greatestDistInfo = (name1, name2, greatestDist)
    
    return greatestDistInfo

if __name__ == "__main__": 
    
    stations = get_station_data('stations1.csv')

    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)

    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)


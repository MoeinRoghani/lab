import csv
from math import radians, sin, cos, sqrt, atan2
from min_heap import MinHeap
from A_star import a_star


#reading london_connections.csv
def connections(csvfile):
    connections = {}
    with open(csvfile, 'r') as filehandle:
        data = csv.DictReader(filehandle)
        for row in data:
            station1 = int(row['station1'])
            station2 = int(row['station2'])
            time = int(row['time'])
            if station1 not in connections:
                connections[station1] = {}
            if station2 not in connections:
                connections[station2] = {}
            connections[station1][station2] = time
            connections[station2][station1] = time
    return connections



global dic_stations
global source_station_id 
global destination_station_id
dic_stations = {}
source_station_id = 1 #Acton
destination_station_id = 11 #Baker 


#this will represent our heuristic dictionary for each station 
def heuristic_func(csvfile):
	heuristic = {}

	#reading london_stations.csv
	#read from csv file
	with open (csvfile, 'r') as filehandle:
		data = csv.DictReader(filehandle)
		for row in data:
		    station_id = int(row['id'])
		    latitude = float(row['latitude'])
		    longitude = float(row['longitude'])
		    name = row['name']
		    dic_stations[station_id] = {'name': name, 'latitude': latitude, 'longitude': longitude}

    #make the heuristic dictionary
	dest_lat = dic_stations[destination_station_id]['latitude']
	dest_lon = dic_stations[destination_station_id]['longitude']
	for station_id, station_data in dic_stations.items():
	    heuristic[station_id] = euclidean_distance(station_data['latitude'], station_data['longitude'], dest_lat, dest_lon)
	return heuristic


#according to geographic information systems (GIS)
#source:https://www.movable-type.co.uk/scripts/latlong.html
def euclidean_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth's radius in km
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c





#-------------------------------------Runner-------------------------------------


# Create the heuristic function for the destination station
heuristic = heuristic_func("data/london_stations.csv")
connections = connections('data/london_connections.csv')

# Run the A* algorithm
predecessors, path = a_star(connections, source_station_id, destination_station_id, heuristic)

# Print the path with station names
print("Shortest path:")
for station_id in path:
    print(dic_stations[station_id]['name'], end=' -> ')
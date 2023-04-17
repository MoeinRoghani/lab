import csv
from math import radians, sin, cos, sqrt, atan2
from min_heap import MinHeap
from A_star import a_star
from final_project_part1 import DirectedWeightedGraph
from dijkstra import dijkstra
import timeit



#reading london_connections.csv
def connections(csvfile):
    connections = {}
    with open(csvfile, 'r') as filehandle:
        data = csv.DictReader(filehandle)
        for row in data:
            station1 = int(row['station1'])
            station2 = int(row['station2'])
            time = int(row['time'])
            line = int(row['line'])
            if station1 not in connections:
                connections[station1] = {}
            # if station2 not in connections:
            #     connections[station2] = {}
            connections[station1][station2] = [time, line]
            # connections[station2][station1] = time
    return connections



global dic_stations
dic_stations = {}



#this will represent our heuristic dictionary for each station 
def heuristic_func(csvfile, destination_station_id):
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

##HEURISTIC WEIGHTED GRAPH
class WeightedGraph(DirectedWeightedGraph):

    def add_edge(self, node1, node2, weight):
        if node2 not in self.adj[node1]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)
        self.weights[(node1, node2)] = weight
        self.weights[(node2, node1)] = weight


def createLondon(csvfile,connection):
    lond = WeightedGraph()
    stations = {}
    with open(csvfile, 'r') as filehandle:
        data = csv.DictReader(filehandle)
        for row in data:
            station_id = int(row['id'])
            latitude = float(row['latitude'])
            longitude = float(row['longitude'])
            name = row['name']
            stations[station_id] = {'name': name, 'latitude': latitude, 'longitude': longitude}

    # ADDING nodes
    for station in stations:
        lond.add_node(station)

    # ADDING edges
    for current in connection:
        current_lat = stations[current]['latitude']
        current_lon = stations[current]['longitude']
        for dest in connection[current]:
            dest_lat = stations[dest]['latitude']
            dest_lon = stations[dest]['longitude']
            weight  = euclidean_distance(current_lat,current_lon, dest_lat, dest_lon)
            lond.add_edge(current, dest, weight)
    return lond




#-------------------------------------Runner-------------------------------------


# Create the heuristic function for the destination station
# heuristic = heuristic_func("data/london_stations.csv", 11)
connections = connections('data/london_connections.csv')
london = createLondon("data/london_stations.csv", connections)

# Run the A* algorithm
# predecessors, path = a_star(london, 1, 11, heuristic)
# # Print the path with station names
# print("Shortest path:")
# for station_id in path:
#     print(dic_stations[station_id]['name'], end=' -> ')

oneLine = WeightedGraph()
stat = {}
with open("data/london_stations.csv", 'r') as filehandle:
    data = csv.DictReader(filehandle)
    for row in data:
        station_id = int(row['id'])
        latitude = float(row['latitude'])
        longitude = float(row['longitude'])
        name = row['name']
        stat[station_id] = {'name': name, 'latitude': latitude, 'longitude': longitude}

# ADDING nodes
for station in stat:
    oneLine.add_node(station)

# ADDING edges
for current in connections:
    current_lat = stat[current]['latitude']
    current_lon = stat[current]['longitude']
    for dest in connections[current]:
        if connections[current][dest][1] == 1:
            dest_lat = stat[dest]['latitude']
            dest_lon = stat[dest]['longitude']
            weight  = euclidean_distance(current_lat,current_lon, dest_lat, dest_lon)
            oneLine.add_edge(current, dest, weight)


#For all adjecent connections
# runDij = 0
# runStar = 0
# for i in range(10):
#     astarTimeTotal = [0, 0]
#     DijTimeTotal = [0, 0]
#     for current in london.adj:
#         for dest in london.adj:
#             if current != dest:
#                 heuristic = heuristic_func("data/london_stations.csv", dest)
#
#                 start = timeit.default_timer()
#                 p,path = a_star(london, current, dest, heuristic)
#                 end = timeit.default_timer()
#                 astarTimeTotal[0] += end - start
#                 astarTimeTotal[1] += 1
#
#                 start = timeit.default_timer()
#                 t = dijkstra(london, current, dest)
#                 end = timeit.default_timer()
#
#                 DijTimeTotal[0] += end - start
#                 DijTimeTotal[1] += 1
#                 print("TTime:",DijTimeTotal[0])
#                 print("TRun:",DijTimeTotal[1])
#                 print(end-start)
#     runDij += DijTimeTotal[0]/DijTimeTotal[1]
#     runStar += astarTimeTotal[0]/astarTimeTotal[1]
# dij = runDij / 10
# star = runStar / 10
# print ("DijTime:" , dij )
# print ("StarTime:" , star)
# print ("A* improvement:", (abs(dij - star)/dij)* 100)

heuristic = heuristic_func("data/london_stations.csv", 246)
start = timeit.default_timer()
p,path = a_star(oneLine, 11,246, heuristic)
end = timeit.default_timer()
print("start",end-start)

start = timeit.default_timer()
t = dijkstra(oneLine, 11, 246)
end = timeit.default_timer()
print("start", end-start)
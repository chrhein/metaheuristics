from dataclasses import dataclass


@dataclass
class Vehicle:
    vehicle_id: int
    home_node: int
    starting_time: int
    capacity: int


with open("assets/Call_18_Vehicle_5.txt", "r") as f:
    file = f.readlines()

line = iter(file)

# number of nodes
next(line)
nodes = int(next(line))

# number of vehicles
next(line)
vehicles = int(next(line))

# for each vehicle: vehicle index, home node, starting time, capacity
next(line)
vehicles_dict = {}
for _ in range(vehicles):
    strList = list(map(int, next(line).split(",")))
    vehicles_dict[strList[0]] = Vehicle(strList[0], strList[1], strList[2], strList[3])


from data_classes import *

with open("assets/Call_7_Vehicle_3.txt", "r") as f:
    file = f.readlines()

line = iter(file)

next(line)

# number of nodes
nodes = int(next(line))

next(line)

# number of vehicles
vehicles = int(next(line))

next(line)

# for each vehicle: vehicle index, home node, starting time, capacity
vehicles_dict = {}
for _ in range(vehicles):
    string_list = list(map(int, next(line).split(",")))
    vehicles_dict[string_list[0]] = Vehicle(string_list[0], string_list[1], string_list[2], string_list[3])

next(line)

# number of calls
calls = int(next(line))

next(line)

# for each vehicle, vehicle index, and then a list of calls that can be transported using that vehicle
for _ in range(vehicles):
    string_list = list(map(int, next(line).split(",")))
    vehicles_dict[string_list[0]].valid_calls.extend(string_list[1:])

next(line)

# for each call: call index, origin node, destination node, size, cost of not transporting, lb tw pu, ub tw pu,
# lb tw d, ub tw d
calls_dict = {}
for _ in range(calls):
    string_list = list(map(int, next(line).split(",")))
    calls_dict[string_list[0]] = Call(string_list[0], string_list[1], string_list[2], string_list[3], string_list[4],
                                      string_list[5], string_list[6], string_list[7], string_list[8])

next(line)

# travel times and costs: vehicle, origin node, destination node, travel time (in hours), travel cost (in €)
routes_dict = {}
for _ in range(vehicles * nodes * nodes):
    string_list = list(map(int, next(line).split(",")))
    e1 = string_list.pop(0)
    e2 = string_list.pop(0)
    e3 = string_list.pop(0)
    key = (e1, e2, e3)
    routes_dict[key] = Travel(e1, e2, e3, string_list[0], string_list[1])

next(line)

# node times and costs: vehicle, call, origin node time (in hours), origin node costs (in €), destination node time
# (in hours), destination node costs (in €)
nodes_costs_dict = {}
for _ in range(calls * vehicles):
    string_list = list(map(int, next(line).split(",")))
    e1 = string_list.pop(0)
    e2 = string_list.pop(0)
    key = (e1, e2)
    nodes_costs_dict[key] = Node(e1, e2, string_list[0], string_list[1], string_list[2])

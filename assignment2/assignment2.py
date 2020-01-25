from dataclasses import dataclass, field
from typing import List


@dataclass
class Vehicle:
    vehicle_id: int
    home_node: int
    starting_time: int
    capacity: int
    valid_calls: List[int] = field(default_factory=lambda: list())


@dataclass
class Call:
    call_index: int
    origin_node: int
    destination_node: int
    size: int
    cost_no_transport: int
    lb_tw_pu: int
    ub_tw_pu: int
    lb_tw_d: int
    ub_tw_d: int


@dataclass
class Route:
    vehicle_id: int
    origin_node: int
    destination_node: int
    travel_time: int
    travel_cost: int


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
    string_list = list(map(int, next(line).split(",")))
    vehicles_dict[string_list[0]] = Vehicle(string_list[0], string_list[1], string_list[2], string_list[3])

# number of calls
next(line)
calls = int(next(line))

# for each vehicle, vehicle index, and then a list of calls that can be transported using that vehicle
next(line)
for _ in range(vehicles):
    string_list = list(map(int, next(line).split(",")))
    vehicles_dict[string_list[0]].valid_calls.extend(string_list[1:])

# for each call: call index, origin node, destination node, size, cost of not transporting, lb tw pu, ub tw pu,
# lb tw d, ub tw d
calls_dict = {}
next(line)
for _ in range(calls):
    string_list = list(map(int, next(line).split(",")))
    calls_dict[string_list[0]] = Call(string_list[0], string_list[1], string_list[2], string_list[3], string_list[4],
                                      string_list[5], string_list[6], string_list[7], string_list[8])

# travel times and costs: vehicle, origin node, destination node, travel time (in hours), travel cost (in €)
routes_dict = {}
next(line)
for _ in range(vehicles * nodes * nodes):
    string_list = list(map(int, next(line).split(",")))
    print(string_list)
    routes_dict[string_list[0]] = Route(string_list[0], string_list[1], string_list[2], string_list[3], string_list[4])

print(routes_dict)

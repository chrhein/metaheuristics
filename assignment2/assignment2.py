import random
from dataclasses import dataclass, field
from typing import List


@dataclass
class Vehicle:
    vehicle_index: int
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


@dataclass
class Travel:
    vehicle_id: int
    origin_node: int
    destination_node: int
    travel_time: int
    travel_cost: int


@dataclass
class Node:
    vehicle_id: int
    origin_node_time: int
    origin_node_costs: int
    dest_node_time: int
    dest_node_costs: int


# the next ~100 lines are for reading input text file
# next(line) skips lines with comments in text file


with open("assets/Call_18_Vehicle_5.txt", "r") as f:
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


def print_input():
    print(nodes)
    print(vehicles)
    print(vehicles_dict)
    print(calls)
    print(calls_dict)
    print(routes_dict)
    print(nodes_costs_dict)


def get_random_call():
    call = calls_dict.get(random.randint(1, calls))
    return call


# function for generating a random solution
def random_solution():
    route = []
    chosen_calls = []
    i = 0
    while len(chosen_calls) < calls:
        vc = vehicles_dict.get(i % vehicles + 1).valid_calls
        i += 1
        call = random.choice(vc)
        if call not in chosen_calls:
            print("Call:", call)
            chosen_calls.append(call)
            print("i: ", i)
            print(vc)
            print(vehicles_dict.get(i % vehicles + 1))
        else:
            continue


    print(chosen_calls)


# print_input()
random_solution()

from dataclasses import dataclass, field
from typing import List


# for each vehicle: vehicle index, home node, starting time, capacity
@dataclass
class Vehicle:
    vehicle_index: int
    home_node: int
    starting_time: int
    capacity: int
    valid_calls: List[int] = field(default_factory=lambda: list())


# for each call: call index, origin node, destination node, size, cost of not transporting, lb tw pu, ub tw pu,
# lb tw d, ub tw d
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


# travel times and costs: vehicle, origin node, destination node, travel time (in hours), travel cost (in €)
@dataclass
class TravelCost:
    vehicle_id: int
    origin_node: int
    destination_node: int
    travel_time: int
    travel_cost: int


# node times and costs: vehicle, call, origin node time (in hours), origin node costs (in €), destination node time
# (in hours), destination node costs (in €)
@dataclass
class NodeCost:
    vehicle_id: int
    origin_node_time: int
    origin_node_costs: int
    dest_node_time: int
    dest_node_costs: int

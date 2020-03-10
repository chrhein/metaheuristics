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

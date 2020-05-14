import random

from tools.route_handler import get_routes_as_list_w_zeroes, list_to_solution

vehicle_index = 0


def x_one_reinserts_inside_vehicle(solution):
    calls = get_routes_as_list_w_zeroes(solution)
    global vehicle_index
    vehicle = calls[vehicle_index]
    if len(vehicle) > 3:
        call = random.choice(vehicle[:-1])
        vehicle.remove(call)
        vehicle.insert(random.randrange(0, len(vehicle[:-1])), call)
    vehicle_index = (vehicle_index + 1) % len(calls[:-1])
    return list_to_solution(calls)

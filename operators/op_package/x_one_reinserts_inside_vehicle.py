import random

from tools.route_handler import get_routes_as_list_w_zeroes, list_to_solution

vehicle_asc = 0
vehicle_dsc = 0


def x_one_reinserts_inside_vehicle(solution):
    calls = get_routes_as_list_w_zeroes(solution)
    global vehicle_asc
    new_sol = x_o(calls, vehicle_asc)
    vehicle_asc = (vehicle_asc + 1) % len(calls[:-1])
    return new_sol


def x_one_reinserts_inside_vehicle_dsc(solution):
    calls = get_routes_as_list_w_zeroes(solution)
    global vehicle_dsc
    new_sol = x_o(calls, vehicle_dsc)
    vehicle_dsc = (vehicle_dsc - 1) % len(calls[:-1])
    return new_sol


def x_o(calls, index):
    vehicle = calls[index]
    if len(vehicle) > 3:
        call = random.choice(vehicle[:-1])
        vehicle.remove(call)
        vehicle.insert(random.randrange(0, len(vehicle[:-1])), call)
    return list_to_solution(calls)


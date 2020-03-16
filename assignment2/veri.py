import file_handler as x


def check_solution(solution):
    current_vehicle_index = 1
    v = x.vehicles_dict
    c = x.calls_dict
    number_of_vehicles = x.vehicles
    currently_transporting_size = 0
    pickups = []
    currently_transporting = []
    for vehicle in v:
        total_time = time_calc(current_vehicle_index, route_planner(solution).get(v.get(vehicle).vehicle_index), v, c)
        current_vehicle_index += 1
        print(total_time)

    current_vehicle_index = 1
    for sol_call in solution:

        # zeroes marks switch of vehicles
        if sol_call == 0:
            current_vehicle_index += 1
            for i in pickups:
                if pickups.count(i) is not 2:
                    return False

            pickups = []
            currently_transporting_size = 0
            continue

        pickups.append(sol_call)

        # checks for all vehicles but the dummy
        if current_vehicle_index < number_of_vehicles + 1:
            vehicle = v.get(current_vehicle_index)
            call = c.get(sol_call)

            # check if call is valid for the current vehicle
            if sol_call not in vehicle.valid_calls:
                return False

            # check if vehicles has capacity for the call size
            capacity = vehicle.capacity
            if sol_call not in currently_transporting:
                currently_transporting.append(sol_call)
                currently_transporting_size += call.size
                if currently_transporting_size > capacity:
                    return False

            else:
                currently_transporting.remove(sol_call)
                currently_transporting_size -= call.size

    return True


def time_calc(vehicle_index, vehicle_route, vehicle_dict, call_dict):
    if not vehicle_route:
        return 0
    c = call_dict
    v = vehicle_dict.get(vehicle_index)
    t = x.travel_cost_dict
    n = x.nodes_costs_dict

    pus = []

    total_duration = v.starting_time
    print("Starting time:", total_duration)
    origin_node = v.home_node
    print("Home node:", origin_node)
    dest_node = c.get(vehicle_route[0]).origin_node
    print("First pu node:", dest_node)
    key = (vehicle_index, origin_node, dest_node)
    total_duration += t.get(key).travel_time
    print("Time used to travel between", origin_node, "and", dest_node, ":", t.get(key).travel_time)

    for call in vehicle_route:
        if vehicle_index == 0 or vehicle_index > x.vehicles:
            print("Vehicle index out of bounds")
            break

        print("Handling call:", call)
        origin_node = c.get(call).origin_node
        print("Origin node:", origin_node)
        dest_node = c.get(call).destination_node
        print("Dest node:", dest_node)

        key = (vehicle_index, call)
        if call not in pus:
            pus.append(call)
            total_duration += n.get(key).origin_node_time
            print("Time used during pick up:", n.get(key).origin_node_time)
            key = (vehicle_index, origin_node, dest_node)
            total_duration += t.get(key).travel_time
            print("Time used to travel between", origin_node, "and", dest_node, ":", t.get(key).travel_time)
        else:
            total_duration += n.get(key).dest_node_time
            print("Time used during delivery:", n.get(key).dest_node_time)

        print("End of handling this call")

    return total_duration


def route_planner(solution):
    s = solution.copy()
    v_index = 1
    v_route = []
    routes = {}
    for _ in s:
        popped = s.pop(0)
        if popped == 0:
            routes[v_index] = v_route
            v_index += 1
            v_route = []
        else:
            v_route.append(popped)

    return routes

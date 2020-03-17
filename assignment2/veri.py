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
        if not total_time:
            return False

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
        return True
    print("Vehicle route from input:", vehicle_route)
    c = call_dict
    v = vehicle_dict.get(vehicle_index)
    t = x.travel_cost_dict
    n = x.nodes_costs_dict

    pus = []

    total_duration = v.starting_time
    print("\nStarting time:", total_duration)
    origin_node = v.home_node
    print("Home node:", origin_node)
    dest_node = c.get(vehicle_route[0]).origin_node
    pus.append(vehicle_route[0])
    print("First pu node:", dest_node)
    key = (vehicle_index, origin_node, dest_node)
    total_duration += t.get(key).travel_time
    print("Time used to travel between", origin_node, "and", dest_node, ":", t.get(key).travel_time)

    rt = calls_to_nodes(vehicle_route)

    call_index = 0

    for call in vehicle_route:

        key = (vehicle_index, call)

        if call not in pus:
            pus.append(call)

            lb_tw_pu = c.get(call).lb_tw_pu
            ub_tw_pu = c.get(call).ub_tw_pu

            if total_duration > ub_tw_pu:
                return False

            if lb_tw_pu > total_duration:
                print("Came before pick up time, has to wait.", total_duration, "<", lb_tw_pu)
                total_duration = lb_tw_pu

            total_duration += n.get(key).origin_node_time
            print("Time used during pick up:", n.get(key).origin_node_time)

            print("Total time should be between:", lb_tw_pu, total_duration, ub_tw_pu)
            key = (vehicle_index, origin_node, dest_node)
            total_duration += t.get(key).travel_time
            print("Time used to travel between", origin_node, "and", dest_node, ":", t.get(key).travel_time)
        else:
            lb_tw_d = c.get(call).lb_tw_d
            ub_tw_d = c.get(call).ub_tw_d

            if lb_tw_d > total_duration:
                print("Came before delivery time, has to wait.", total_duration, "<", lb_tw_d)
                total_duration = lb_tw_d

            key = (vehicle_index, call)
            total_duration += n.get(key).dest_node_time

            if total_duration > ub_tw_d:
                return False

        print("End of handling this call \n")

    return True


def calls_to_nodes(vehicle_route):
    pu = []
    route_in_nodes = []
    for call in vehicle_route:
        o = x.calls_dict.get(call).origin_node
        d = x.calls_dict.get(call).destination_node
        if call not in pu:
            pu.append(call)
            route_in_nodes.append(o)
        else:
            route_in_nodes.append(d)
    return route_in_nodes


def route_planner(solution):
    s = solution.copy()
    v_index = 1
    v_route = []
    routes = {}
    size = len(s)
    for _ in range(size):
        popped = s.pop(0)
        if popped == 0:
            routes[v_index] = v_route
            v_index += 1
            v_route = []
        else:
            v_route.append(popped)
    return routes

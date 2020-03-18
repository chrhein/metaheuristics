import file_handler as x


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


def time_cost_calc(vehicle_index, vehicle_route, vehicle_dict, call_dict):
    if not vehicle_route:
        return [True, 0]
    c = call_dict
    v = vehicle_dict.get(vehicle_index)
    t = x.travel_cost_dict
    n = x.nodes_costs_dict

    pus = []

    total_duration = v.starting_time
    total_cost = 0
    origin_node = v.home_node
    dest_node = 0

    rt = calls_to_nodes(vehicle_route)
    # print("Route for vehicle %d: %d" % (vehicle_index, origin_node), " ".join(str(i) for i in rt))
    call_index = 0

    for i in range(len(rt) - 1):
        node = rt[i]
        call = vehicle_route[call_index]

        if call_index == 0:
            dest_node = node

            key = (vehicle_index, origin_node, dest_node)
            total_duration += t.get(key).travel_time
            total_cost += t.get(key).travel_cost

        origin_node = dest_node
        dest_node = rt[i + 1]

        key = (vehicle_index, call)
        if call not in pus:
            pus.append(call)

            lb_tw_pu = c.get(call).lb_tw_pu
            ub_tw_pu = c.get(call).ub_tw_pu

            if total_duration > ub_tw_pu:
                print("Missed upper bound time window for pickup.")
                print("Total duration was %d, while upper bound time window was %d" % (total_duration, ub_tw_pu))
                return [False, 0]

            if lb_tw_pu > total_duration:
                total_duration = lb_tw_pu

            total_duration += n.get(key).origin_node_time
            total_cost += n.get(key).origin_node_costs

            key = (vehicle_index, origin_node, dest_node)
            total_duration += t.get(key).travel_time
            total_cost += t.get(key).travel_cost
        else:
            lb_tw_d = c.get(call).lb_tw_d
            ub_tw_d = c.get(call).ub_tw_d

            if lb_tw_d > total_duration:
                total_duration = lb_tw_d

            total_duration += n.get(key).dest_node_time
            total_cost += n.get(key).dest_node_costs

            if total_duration > ub_tw_d:
                print("Missed upper bound time window for delivery.")
                print("Total duration was %d, while upper bound time window was %d" % (total_duration, ub_tw_d))
                return [False, 0]

        call_index += 1
    return [True, total_cost]


def check_solution(solution):
    current_vehicle_index = 1
    v = x.vehicles_dict
    c = x.calls_dict
    number_of_vehicles = x.vehicles
    currently_transporting_size = 0
    pickups = []
    currently_transporting = []

    for sol_call in solution:

        # zeroes marks switch of vehicles
        if sol_call == 0:
            current_vehicle_index += 1
            for i in pickups:
                if pickups.count(i) is not 2:
                    print("A call is picked up, but not delivered.")
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
                print("Invalid call for this vehicle.")
                return False

            # check if vehicles has capacity for the call size
            capacity = vehicle.capacity
            if sol_call not in currently_transporting:
                currently_transporting.append(sol_call)
                currently_transporting_size += call.size
                if currently_transporting_size > capacity:
                    print("Capacity overload.")
                    return False

            else:
                currently_transporting.remove(sol_call)
                currently_transporting_size -= call.size

    current_vehicle_index = 1
    freight_cost = 0
    dummy_cost_no_transport = 0
    for vehicle in v:
        tcc = time_cost_calc(current_vehicle_index,
                             route_planner(solution).get(v.get(vehicle).vehicle_index), v, c)
        total_time = tcc[0]
        freight_cost += tcc[1]
        current_vehicle_index += 1
        if not total_time:
            return False

    dummy_calls = solution[::-1]
    dummy_pus = []
    for i in dummy_calls:
        if i == 0:
            break
        if i not in dummy_pus:
            dummy_pus.append(i)

    for i in dummy_pus:
        dummy_cost_no_transport += c.get(i).cost_no_transport

    total_cost = freight_cost + dummy_cost_no_transport

    print("Total cost:", total_cost)

    return True

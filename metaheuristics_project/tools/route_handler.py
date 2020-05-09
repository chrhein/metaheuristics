from setup import file_handler as x


def calls_to_nodes(vehicle_route):
    pu = []
    route_in_nodes = []
    for call in vehicle_route:
        o = x.calls_dict[call].origin_node
        d = x.calls_dict[call].destination_node
        if call not in pu:
            pu.append(call)
            route_in_nodes.append(o)
        else:
            route_in_nodes.append(d)

    return route_in_nodes


def route_planner(solution):
    v_index = 1
    v_route = []
    routes = {}
    for i in range(len(solution)):
        popped = solution[i]
        if popped == 0:
            routes[v_index] = v_route
            v_index += 1
            v_route = []
        else:
            v_route.append(popped)
    return routes


def get_calls_including_zeroes(solution):
    calls = {}
    vehicle_calls = []
    vehicle_index = 1
    for call in solution:
        if call == 0:
            vehicle_calls.append(call)
            calls[vehicle_index] = vehicle_calls
            vehicle_index += 1
            vehicle_calls = []
        else:
            vehicle_calls.append(call)
    calls[vehicle_index] = vehicle_calls
    return calls


def get_index_positions(list_of_elements, element):
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            index_pos = list_of_elements.index(element, index_pos)
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break

    return index_pos_list


def get_most_expensive_calls(solution):
    calls = {}
    for call in solution:
        if call != 0:
            calls[call] = x.calls_dict[call].cost_no_transport
    sorted_calls_by_value = {k: v for k, v in sorted(calls.items(), key=lambda item: item[1], reverse=True)}
    return sorted_calls_by_value


def most_expensive_dummy(solution):
    dummy_calls = get_calls_including_zeroes(solution)[x.vehicles + 1]
    return get_most_expensive_calls(dummy_calls)


def calls_to_solution(calls_dict):
    new_solution = []
    for val in calls_dict.values():
        for call in val:
            new_solution.append(call)
    return new_solution


def list_to_solution(calls_list):
    new_solution = []
    for val in calls_list:
        for call in val:
            new_solution.append(call)
    return new_solution


def get_routes_as_list(solution):
    vehicles = []
    route = []
    for i in range(len(solution)):
        if solution[i] == 0:
            vehicles.append(route)
            route = []
        else:
            route.append(solution[i])
    return vehicles


def get_routes_as_list_w_zeroes(solution):
    vehicles = []
    route = []
    for i in range(len(solution)):
        if solution[i] == 0:
            route.append(solution[i])
            vehicles.append(route)
            route = []
        else:
            route.append(solution[i])
    vehicles.append(route)
    return vehicles

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

import file_handler as x
import route_handler as rh


def cost_calc(solution):
    current_vehicle_index = 0
    total_cost = 0
    c = x.calls_dict
    t = x.travel_cost_dict
    n = x.nodes_costs_dict
    for vehicle in x.vehicles_dict:
        current_vehicle_index += 1
        vehicle_route = rh.route_planner(solution).get(x.vehicles_dict.get(vehicle).vehicle_index)
        if not vehicle_route:
            continue
        v = x.vehicles_dict.get(current_vehicle_index)
        calls_onboard = []
        origin_node = v.home_node
        rt = rh.calls_to_nodes(vehicle_route)
        dest_node = rt.pop(0)
        call_index = 0
        for i in range(len(vehicle_route)):
            call = vehicle_route[call_index]
            if call_index == 0:
                key = (current_vehicle_index, origin_node, dest_node)
                total_cost += t.get(key).travel_cost
            origin_node = dest_node
            try:
                dest_node = rt.pop(0)
            except IndexError as e:
                dest_node = -1
            key = (current_vehicle_index, call)
            if call not in calls_onboard and dest_node != -1:
                calls_onboard.append(call)
                total_cost += n.get(key).origin_node_costs
            else:
                calls_onboard.remove(call)
                total_cost += n.get(key).dest_node_costs
            try:
                key = (current_vehicle_index, origin_node, dest_node)
                total_cost += t.get(key).travel_cost
            except AttributeError as a:
                break
            call_index += 1
    dummy_cost_no_transport = 0
    dummy_calls = solution[::-1]
    dummy_pus = []
    for i in dummy_calls:
        if i == 0:
            break
        if i not in dummy_pus:
            dummy_pus.append(i)
    for i in dummy_pus:
        dummy_cost_no_transport += c.get(i).cost_no_transport
    total_cost += dummy_cost_no_transport
    return total_cost

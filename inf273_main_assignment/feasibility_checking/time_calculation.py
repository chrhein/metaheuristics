from setup import file_to_dataclass as x
from tools.route_handler import calls_to_nodes


def time_calc(vehicle_index, vehicle_route, vehicle_dict, call_dict):
    if not vehicle_route:
        return True
    c = call_dict
    v = vehicle_dict.get(vehicle_index)
    t = x.travel_cost_dict
    n = x.nodes_costs_dict
    calls_onboard = []
    local_time = v.starting_time
    origin_node = v.home_node
    rt = calls_to_nodes(vehicle_route)
    dest_node = rt.pop(0)
    call_index = 0
    for i in range(len(vehicle_route)):
        call = vehicle_route[call_index]
        if call_index == 0:
            key = (vehicle_index, origin_node, dest_node)
            local_time += t.get(key).travel_time
        origin_node = dest_node
        try:
            dest_node = rt.pop(0)
        except IndexError as e:
            dest_node = -1
        key = (vehicle_index, call)
        if call not in calls_onboard and dest_node != -1:
            calls_onboard.append(call)
            lb_tw_pu = c.get(call).lb_tw_pu
            ub_tw_pu = c.get(call).ub_tw_pu
            if local_time > ub_tw_pu:
                # print("Missed upper bound time window for pickup.")
                # print("Time is now %d, while upper bound time window was %d." % (local_time, ub_tw_pu))
                return False
            if lb_tw_pu > local_time:
                local_time = lb_tw_pu
            local_time += n.get(key).origin_node_time
        else:
            calls_onboard.remove(call)
            lb_tw_d = c.get(call).lb_tw_d
            ub_tw_d = c.get(call).ub_tw_d
            if lb_tw_d > local_time:
                local_time = lb_tw_d
            if local_time > ub_tw_d:
                # print("Missed upper bound time window for delivery.")
                # print("Time is now %d, while upper bound time window was %d." % (local_time, ub_tw_d))
                return False
            local_time += n.get(key).dest_node_time
        try:
            key = (vehicle_index, origin_node, dest_node)
            local_time += t.get(key).travel_time
        except AttributeError as a:
            break
        call_index += 1
    return True

from setup import file_handler as x


def print_input():
    print("Number of nodes: ", x.nodes)
    print("Number of vehicles: ", x.vehicles)
    print("Vehicle dataclasses: ", x.vehicles_dict)
    print("Number of calls: ", x.calls)
    print("Call dataclasses: ", x.calls_dict)
    print("Travel times and costs: ", x.travel_cost_dict)
    print("Node times and costs: ", x.nodes_costs_dict)


print_input()

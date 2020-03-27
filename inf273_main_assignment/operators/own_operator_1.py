import random

import setup.file_handler as x
from tools.calls_dict_to_solution import calls_to_solution
from tools.route_handler import get_calls_including_zeroes, get_most_expensive_calls


def one_insert_most_expensive_call(solution):
    calls = get_calls_including_zeroes(solution)
    if not calls[x.vehicles + 1]:
        return solution
    cost_no_transport = get_most_expensive_calls(solution)
    cnt_list = list(cost_no_transport.keys())
    if not cnt_list or len(cnt_list) < 3:
        return solution
    most_expensive_call = cnt_list[random.randrange(0, 3)]
    # most_expensive_call = max(cost_no_transport, key=cost_no_transport.get)
    if most_expensive_call in calls[x.vehicles + 1]:
        calls[x.vehicles + 1].remove(most_expensive_call)
        calls[x.vehicles + 1].remove(most_expensive_call)
        for i in range(1, x.vehicles + 1):
            vehicle = x.vehicles_dict[i]
            if most_expensive_call in vehicle.valid_calls:
                calls[i].insert(random.randrange(0, len(calls[i])), most_expensive_call)
                calls[i].insert(random.randrange(0, len(calls[i])), most_expensive_call)
                break

    # most_expensive_cost_of_no_transport = max(x.calls_dict.get(c).cost_no_transport for c in calls[x.vehicles+1])
    # call_most_expensive_no_transport = \
    #     list(calls.keys())[list(calls.values()).index(most_expensive_cost_of_no_transport)]
    # print("Call:", call_most_expensive_no_transport)
    # print("Cost:",most_expensive_cost_of_no_transport)
    return calls_to_solution(calls)

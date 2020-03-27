import random

from feasibility_checking.cost_calculation import f
from operators.basic_operators import one_reinsert, two_exchange, three_exchange
from tools.route_handler import get_calls_including_zeroes, get_most_expensive_calls
import setup.file_handler as x


def one_insert_most_expensive_call(solution):
    calls = get_calls_including_zeroes(solution)
    cost_no_transport = get_most_expensive_calls(solution)
    most_expensive_call = max(cost_no_transport, key=cost_no_transport.get)
    if most_expensive_call in calls[x.vehicles+1]:
        calls[x.vehicles + 1].remove(most_expensive_call)
        calls[x.vehicles + 1].remove(most_expensive_call)
        for i in range(1, x.vehicles+1):
            vehicle = x.vehicles_dict[i]
            if most_expensive_call in vehicle.valid_calls:
                calls[i].insert(random.randrange(0, len(calls[i])), most_expensive_call)
                calls[i].insert(random.randrange(0, len(calls[i])), most_expensive_call)
                break

    print(calls)
    # most_expensive_cost_of_no_transport = max(x.calls_dict.get(c).cost_no_transport for c in calls[x.vehicles+1])
    # call_most_expensive_no_transport = \
    #     list(calls.keys())[list(calls.values()).index(most_expensive_cost_of_no_transport)]
    # print("Call:", call_most_expensive_no_transport)
    # print("Cost:",most_expensive_cost_of_no_transport)
    return solution

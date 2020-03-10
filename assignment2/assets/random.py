import random

import file_handler as x


def random_solution():
    random_calls = []
    for i in range(1, x.calls + 1):
        random_calls.append(i)
        random_calls.append(i)
    for i in range(x.vehicles):
        random_calls.append(0)
    random.shuffle(random_calls)
    return random_calls

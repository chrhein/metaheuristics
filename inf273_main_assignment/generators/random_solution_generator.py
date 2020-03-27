import random

from setup import file_handler as x


def random_solution():
    random_calls = []
    for i in range(x.calls):
        random_calls.append(i + 1)
        random_calls.append(i + 1)
    for i in range(x.vehicles):
        random_calls.append(0)
    random.shuffle(random_calls)
    return random_calls

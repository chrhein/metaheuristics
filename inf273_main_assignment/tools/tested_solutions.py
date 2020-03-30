seen_before = []


def seen(solution):
    global seen_before
    seen_before.append(solution)


def clear_seen():
    global seen_before
    seen_before = []


def in_seen_before():
    global seen_before
    return seen_before

def badge_maker(name):
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    return [badge_maker(name) for name in names]


def assign_rooms(names):
    return [
        f"Hello, {name}! You'll be assigned to room {i}!"
        for i, name in enumerate(names, 1)
    ]


def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for room in assign_rooms(names):
        print(room)

# When a variable is creaeted inside a function, it is local
def print_twice(whatever_name):
    print(whatever_name)
    print(whatever_name)


def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)


cat_twice("cat", "cat2")
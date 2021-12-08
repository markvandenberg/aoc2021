def countfishes(fish, days, cache):
    childcount = 0
    for day in range(days):
        if fish == 0:
            key = '{}-{}'.format(fish, days - day - 1)
            sub = cache[key] if key in cache.keys() else countfishes(8, days - day - 1, cache)
            cache.update({key: sub})
            childcount += sub
            fish = 6
        else:
            fish -= 1

    return 1 + childcount

with open("./06/data.txt", "r") as data:
    lines = [line[:-1] for line in data.readlines()]

    cache = {}
    count = 0
    days = 256
    fishes = [int(f) for f in lines[0].split(',')]
    for fish in fishes:
        count += countfishes(fish, days, cache)

    print(count)

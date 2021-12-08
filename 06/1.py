def countfishes(fish, afterdays):
    childcount = 0
    for day in range(afterdays):
        if fish == 0:
            childcount += countfishes(8, afterdays - day - 1)
            fish = 6
        else:
            fish -= 1

    return 1 + childcount

with open("./06/data.txt", "r") as data:
    lines = [line[:-1] for line in data.readlines()]

    count = 0
    fishes = [int(f) for f in lines[0].split(',')]
    for fish in fishes:
        count += countfishes(fish, 80)
    
    print(count)

with open("./02/2.txt", "r") as data:
    values = [[c, int(x)] for c, x in [line.split() for line in data.readlines()]]

    forward = 0
    depth = 0
    aim = 0
    for value in values:
        if value[0] == 'forward':
            forward += value[1]
            depth += aim * value[1]
        elif value[0] == 'down':
            aim += value[1]
        else:
            aim -= value[1]

    print(forward * depth)

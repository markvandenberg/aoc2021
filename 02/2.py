with open("./02/2.txt", "r") as data:
    values = [line.split() for line in data.readlines()]

    forward = 0
    depth = 0
    aim = 0
    for value in values:
        if value[0] == 'forward':
            forward += int(value[1])
            depth += aim * int(value[1])
        if value[0] == 'down':
            aim += int(value[1])
        if value[0] == 'up':
            aim -= int(value[1])

    position = forward * depth
    print(position)

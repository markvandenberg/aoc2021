with open("./02/1.txt", "r") as file1:
    values = [line.split() for line in file1.readlines()]

    forward = sum([int(i[1]) for i in values if i[0] == 'forward'])
    down = sum([int(i[1]) for i in values if i[0] == 'down']) - sum([int(i[1]) for i in values if i[0] == 'up'])

    position = forward * down
    print(position)
    
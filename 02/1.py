with open("./02/1.txt", "r") as data:
    values = [[c, int(x)] for c, x in [line.split() for line in data.readlines()]]
    
    forward = sum([i[1] for i in values if i[0] == 'forward'])
    down = sum([i[1] for i in values if i[0] == 'down']) - sum([i[1] for i in values if i[0] == 'up'])

    print(forward * down)

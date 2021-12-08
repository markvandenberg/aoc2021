with open("./05/data.txt", "r") as data:
    lines = [line[:-1] for line in data.readlines()]

    register = {}

    for line in lines:
        x1 = int(line.split(' -> ')[0].split(',')[0])
        y1 = int(line.split(' -> ')[0].split(',')[1])
        x2 = int(line.split(' -> ')[1].split(',')[0])
        y2 = int(line.split(' -> ')[1].split(',')[1])
        
        difx = x2 - x1 if x1 < x2 else x1 - x2
        dify = y2 - y1 if y1 < y2 else y1 - y2
        forrange =  difx if difx != 0 else dify

        dirx = 1 if x1 < x2 else 0 if x1 == x2 else -1
        diry = 1 if y1 < y2 else 0 if y1 == y2 else -1
        
        for x in range(0, forrange + 1):
            key = "{},{}".format(x1 + (x * dirx), y1 + (x * diry))
            v = register[key] + 1 if key in register.keys() else 1
            register.update({key: v})
    
    count = len([item for item in register if register[item] > 1])
    print(count)
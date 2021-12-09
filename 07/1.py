from statistics import median

with open("./07/data.txt", "r") as data:
    lines = [line[:-1] for line in data.readlines()]
    crabs = [int(f) for f in lines[0].split(',')]

    m = int(median(crabs))
    fuel_cost = sum([abs(crab - m) for crab in crabs])
    
    print(fuel_cost)

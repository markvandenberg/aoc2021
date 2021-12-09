def calc_fuel(n):
    for i in range(int(n)):
        n += i
    return n

with open("./07/data.txt", "r") as data:
    lines = [line[:-1] for line in data.readlines()]
    crabs = [int(f) for f in lines[0].split(',')]
    
    average = int(sum(crabs) / len(crabs))
    fuel_cost = sum([calc_fuel(abs(crab - average)) for crab in crabs])
    
    print(fuel_cost)

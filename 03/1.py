with open("./03/data.txt", "r") as data:
    values = [line[:-1] for line in data.readlines()]

    border = len(values) / 2
    gamma = ''

    for i in range(12):
        gamma += '1' if sum(int(value[i]) for value in values) > border else '0'

    epsilon = ''.join(['1' if i == '0' else '0' for i in gamma])

    print(int(gamma, 2) * int(epsilon, 2))

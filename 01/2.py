with open("./01/1.txt", "r") as data:
    values = [int(line) for line in data.readlines()]

    count = 0

    for i, j in enumerate(values[:-3]):
        sum1 = values[i+2] + values[i+1] + j
        sum2 = values[i+3] + values[i+2] + values[i+1]
        if sum2 > sum1: 
            count += 1

    print(count)

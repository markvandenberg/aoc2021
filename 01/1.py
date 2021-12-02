with open("./01/1.txt", "r") as data:
    values = [int(line) for line in data.readlines()]
 
    count = 0

    for i, j in enumerate(values[:-1]):
        if int(values[i+1]) > int(j): 
            count += 1

    print(count)

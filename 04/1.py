with open("./04/data.txt", "r") as data:
    lines = [line[:-1] for line in data.readlines()]

    numbers = [int(n) for n in lines[0].split(',')]
    boardlines = lines[2:]

    lastnumber = 0
    completeset = []
    rows = []
    columns = []
    temp = [[],[],[],[],[]]
    count = 0
    for line in boardlines:
        if len(line) > 0:
            split = [int(n) for n in line.split()]
            rows.append(split)
            for i in range(5):
                temp[i].append(int(split[i]))
        else:
            for t in temp:
                columns.append(t)
            temp = [[],[],[],[],[]]

    for i in range(len(numbers)):
        if lastnumber > 0:
                break
        
        boardrow = 0
        for j in range(len(rows)):
            if set(rows[j]).issubset(set(numbers[:i])):
                lastnumber = numbers[i-1]
            if set(columns[j]).issubset(set(numbers[:i])):
                lastnumber = numbers[i]

            
            if lastnumber > 0:
                for br in range(j - boardrow, j - boardrow + 5):
                    completeset.extend(set(rows[br]).difference(set(numbers[:i])))
                break
            boardrow += 1 if boardrow < 4 else -4

    print(sum(completeset) * lastnumber)
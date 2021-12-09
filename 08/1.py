with open("./08/data.txt", "r") as data:
    lines = [line[:-1] for line in data.readlines()]
    data = [line.split(' | ')[1] for line in lines]
    
    count = 0
    for digits in data:
        count += len([digit for digit in digits.split() if len(digit) in [2,3,4,7]])
    print(count)

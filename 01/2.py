# Using readlines()
file1 = open("./01/2.txt", "r")
lines = file1.readlines()

count = 0

for i, j in enumerate(lines[:-3]):
    sum1 = int(lines[i+2]) + int(lines[i+1]) + int(j)
    sum2 = int(lines[i+3]) + int(lines[i+2]) + int(lines[i+1])
    if sum2 > sum1: 
        count += 1

print(count)

# Using readlines()
file1 = open("./01/1.txt", "r")
lines = file1.readlines()

count = 0

for i, j in enumerate(lines[:-1]):
    if int(lines[i+1]) > int(j): 
        count += 1

print(count)

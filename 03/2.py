def find(list, index, compare, border):
    if sum(int(item[index]) for item in list) >= border:
        return [item for item in list if item[index] == compare]
    else:
        return [item for item in list if item[index] != compare]


with open("./03/data.txt", "r") as data:
    values = [line[:-1] for line in data.readlines()]

    oxylst = values.copy()
    border = len(oxylst) / 2
    i = 0
    while len(oxylst) > 1:
        oxylst = find(oxylst, i, '1', border)
        border = len(oxylst) / 2
        i = 0 if 1 >= 12 else i + 1

    co2lst = values.copy()
    border = len(co2lst) / 2
    i = 0
    while len(co2lst) > 1:
        co2lst = find(co2lst, i, '0', border)
        border = len(co2lst) / 2
        i = 0 if 1 >= 12 else i + 1

    oxygen = oxylst[0]
    co2 = co2lst[0]
    print(int(oxygen, 2) * int(co2, 2))

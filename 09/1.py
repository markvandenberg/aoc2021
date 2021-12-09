with open("./09/data.txt", "r") as data:
    lines = [line[:-1] for line in data.readlines()]
    risk_level = 0

    for i, line in enumerate(lines):
        for j, chr in enumerate(line):
            point = int(chr)
            up = 9 if i < 1 else int(lines[i - 1][j])
            down = 9 if i >= len(lines) - 1 else int(lines[i + 1][j])
            left = 9 if j < 1 else int(line[j - 1])
            right = 9 if j >= len(line) - 1 else int(line[j + 1])
            if point < up and point < down and point < left and point < right:
                risk_level += point + 1

    print(risk_level)

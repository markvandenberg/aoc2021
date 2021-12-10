from typing import Match

def clean_line(line):
    while len(line) > 0:
        line = line.replace('()','')
        line = line.replace('[]','')
        line = line.replace('{}','')
        line = line.replace('<>','')

        if line.count('()') < 1 and line.count('[]') < 1 and line.count('{}') < 1 and line.count('<>') < 1:
            break

    return line

def score_if_corrupted_line(line):
    score = 0
    illegal_chars = [ic for ic in line if ic in [')',']','}','>']]
    if  len(illegal_chars) > 0:
        match illegal_chars[0]:
            case ')':
                score += 3
            case ']':
                score += 57
            case '}':
                score += 1197
            case '>':
                score += 25137

    return score

with open("./10/data.txt", "r") as data:
    lines = [line[:-1] for line in data.readlines()]

    score = 0
    for line in lines:
        cleaned = clean_line(line)
        score += score_if_corrupted_line(cleaned)
                
    print(score)

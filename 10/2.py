from typing import Match
from statistics import median

def clean_line(line):
    while len(line) > 0:
        line = line.replace('()','')
        line = line.replace('[]','')
        line = line.replace('{}','')
        line = line.replace('<>','')

        if line.count('()') < 1 and line.count('[]') < 1 and line.count('{}') < 1 and line.count('<>') < 1:
            break

    return line

def is_corrupted_line(line):
    illegal_chars = [ic for ic in line if ic in [')',']','}','>']]
    return len(illegal_chars) > 0

def score_cleaned_line(line):
    score = 0
    for char in line[::-1]:
        match char:
            case '(':
                score = score * 5 + 1
            case '[':
                score = score * 5 + 2
            case '{':
                score = score * 5 + 3
            case '<':
                score = score * 5 + 4

    return score

with open("./10/data.txt", "r") as data:
    lines = [line[:-1] for line in data.readlines()]

    scores = []
    for i, line in enumerate(lines):
        cleaned = clean_line(line)

        if is_corrupted_line(cleaned):
            continue

        scores.append(score_cleaned_line(cleaned))
    
    score = sorted(scores)[int(len(scores)/2)]
    print(score)

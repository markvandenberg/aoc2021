def decode_digits(input):
    digits = [''] * 10

    # dfgabce cadfgb cefa ca aecbg dfcegb geabd ecbfg cab agcfbe
    digits[1] = [digit for digit in input if len(digit) == 2][0]
    digits[4] = [digit for digit in input if len(digit) == 4][0]
    digits[7] = [digit for digit in input if len(digit) == 3][0]
    digits[8] = [digit for digit in input if len(digit) == 7][0]

    for digit in [i for i in input if len(i) == 6]:
        if len(set(digits[1]).difference(set(digit))) == 0 and len(set(digits[4]).difference(set(digit))) == 0:
            digits[9] = digit
        if len(set(digits[1]).difference(set(digit))) == 1 and len(set(digits[4]).difference(set(digit))) == 1:
            digits[6] = digit
        if len(set(digits[1]).difference(set(digit))) == 0 and len(set(digits[4]).difference(set(digit))) == 1:
            digits[0] = digit

    for digit in [i for i in input if len(i) == 5]:
        if len(set(digit).intersection(set(digits[6]))) == 5:
            digits[5] = digit

    for digit in [i for i in input if len(i) == 5]:
        if len(set(digit).difference(set(digits[5]))) == 2:
            digits[2] = digit
        if len(set(digit).difference(set(digits[5]))) == 1:
            digits[3] = digit

    return digits

with open("./08/data.txt", "r") as data:
    lines = [line[:-1] for line in data.readlines()]

    count = 0

    for line in [line.split(' | ') for line in lines]:

        digits = decode_digits(line[0].split())
        
        decoded_numbers = ''
        for number in line[1].split():
            for i, digit in enumerate(digits):
                if len(set(digit).difference(set(number))) == 0 and len(set(number).difference(set(digit))) == 0:
                    decoded_numbers += '{}'.format(i)

        count += int(decoded_numbers)

    print(count)

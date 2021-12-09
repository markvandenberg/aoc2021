import collections

def new_basin_nr(pool_values):
    if len(pool_values) > 0:
        return max(pool_values) + 1
    return 0

def update_left(register, i, j, basin_nr):
    key = '{}-{}'.format(i, j - 1)
    if key in register.keys() and register[key] != -1:
        register[key] = basin_nr
        update_left(register, i, j - 1, basin_nr)
        update_up(register, i, j - 1, basin_nr)

def update_up(register, i, j, basin_nr):
    key = '{}-{}'.format(i - 1, j)
    if key in register.keys() and register[key] != -1:
        register[key] = basin_nr
        update_up(register, i - 1, j, basin_nr)
        update_left(register, i - 1, j, basin_nr)
        update_right(register, i - 1, j, basin_nr)

def update_right(register, i, j, basin_nr):
    key = '{}-{}'.format(i, j + 1)
    if key in register.keys() and register[key] != -1:
        register[key] = basin_nr

def print_basin(register):
    prev_line = ''
    for key in register:
        if key.split('-')[0] != prev_line:
            print('')
            prev_line = key.split('-')[0]

        val = '{}'.format(register[key])
        print(val[len(val) - 1:] if register[key] >= 0 else ' ', end='')

    print('')
 
with open("./09/data.txt", "r") as data:
    lines = [line[:-1] for line in data.readlines()]
    basin_register = {}

    for i, line in enumerate(lines):
        for j, chr in enumerate(line):
            if int(chr) < 9:
                keyleft = 'no-key' if j < 1 else '{}-{}'.format(i, j - 1)
                keyup = 'no-key' if i < 1 else  '{}-{}'.format(i - 1, j)
                if keyup in basin_register.keys() and basin_register[keyup] != -1:
                    basin_register['{}-{}'.format(i, j)] = basin_register[keyup]
                    update_left(basin_register, i, j, basin_register[keyup])
                elif keyleft in basin_register.keys() and basin_register[keyleft] != -1:
                    basin_register['{}-{}'.format(i, j)] = basin_register[keyleft]
                else:
                    basin_register['{}-{}'.format(i, j)] = new_basin_nr(basin_register.values())
            else:
                basin_register['{}-{}'.format(i, j)] = -1

    print_basin(basin_register)
    
    counter=collections.Counter([value for value in basin_register.values() if value != -1])
    basin_sizes = [size for size in sorted(counter.values(), reverse=True)]
    print(basin_sizes[0]*basin_sizes[1]*basin_sizes[2])

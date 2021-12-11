def level_up(grid):
    for i, row in enumerate(grid):
        for j, octo in enumerate(row):
            grid[i][j] += 1

def did_octo_flash(grid):
    register = {}
    for i, row in enumerate(grid):
        for j, octo in enumerate(row):
            check_flash(register, grid, i, j)

def check_flash(register, grid, i, j):
    key = '{}-{}'.format(i,j)
        
    if grid[i][j] > 9 and not register.get(key, False):
        register.update({key: True})
        # up
        if i > 0 and grid[i-1][j] <= 9: 
            grid[i-1][j] += 1 
            check_flash(register, grid, i-1, j)
        # down
        if i < 9 and grid[i+1][j] <= 9:
            grid[i+1][j] += 1 
            check_flash(register, grid, i+1, j)
        # left
        if j > 0 and grid[i][j-1] <= 9:
            grid[i][j-1] += 1 
            check_flash(register, grid, i, j-1)
        # right
        if j < 9 and grid[i][j+1] <= 9:
            grid[i][j+1] += 1 
            check_flash(register, grid, i, j+1)
        # up left
        if i > 0 and j > 0 and grid[i-1][j-1] <= 9:
            grid[i-1][j-1] += 1 
            check_flash(register, grid, i-1, j-1)
        # up right
        if i > 0 and j < 9 and grid[i-1][j+1] <= 9:
            grid[i-1][j+1] += 1 
            check_flash(register, grid, i-1, j+1)
        # down left
        if i < 9 and j > 0 and grid[i+1][j-1] <= 9:
            grid[i+1][j-1] += 1 
            check_flash(register, grid, i+1, j-1)
        # down right
        if i < 9 and j < 9 and grid[i+1][j+1] <= 9:
            grid[i+1][j+1] += 1 
            check_flash(register, grid, i+1, j+1)
    
def get_octo_grid(lines):
    grid = [[0]*10,[0]*10,[0]*10,[0]*10,[0]*10,[0]*10,[0]*10,[0]*10,[0]*10,[0]*10]
    for i, row in enumerate(lines):
        for j, octo in enumerate(row):
            grid[i][j] = int(octo)

    return grid

def flash_count(grid):
    count = 0
    
    for i, row in enumerate(grid):
        for j, octo in enumerate(row):
            if grid[i][j] > 9:
                count += 1
                grid[i][j] = 0

    return count

with open("./11/data.txt", "r") as data:
    lines = [line[:-1] for line in data.readlines()]
    grid = get_octo_grid(lines)
    total_flashes = 0

    for step in range(100):
        level_up(grid)
        did_octo_flash(grid)
        total_flashes += flash_count(grid)
   
    print(total_flashes)

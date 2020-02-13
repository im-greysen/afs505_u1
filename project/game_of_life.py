from sys import argv


rows = 30
columns = 80

def start_grid(rows, columns):

    grid = [rows, columns]
    for row in range(rows):
        grid_row = []
        for cols in range(columns):
            if grid_row == 0:
                grid_row += [1]
            else:
                grid_row += [0]

        grid += [grid_row]

    return grid

def print_grid(generation, rows, columns, grid):

    for row in range(rows):
        for cols in range(columns):
            if grid[row][col] == 0:
                str_out += '-'
            else:
                str_out += 'X'
        str_out += "\n\r"

    print(str_out, end=" ")

def new_grid(rows, columns, grid, next_grid):
#  dems da rules
    for row in range(rows):
        for cols in range(columns):

            neigbor = live_neighbor(row, cols, rows, columns, grid)

            if neighbor < 2 or neighbor > 3:
                next_grid[row][cols] = 0

            elif neighbor == 3 and grid[row][cols] == 0:
                next_grid[row][cols] = 1

            else:
                next_grid[row][cols] = grid[row][cols]


def neighbor_status(row, cols, rows, columns, grid):

    life = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if not (i == 0 and j == 0):
                life += grid[((row + i) % rows)][((cols + j) % columns)]
    return life


def move_grid(rows, columns, grid):

    for row in range(rows):
        for cols in range(columns):
            if not (grid[rows][columns] == next_grid[rows][columns]):
                return True
    return False

def main(argv):

    rows = 30
    columns = 80
    generations = 50

    grid = [rows, columns]

    current_gen = start_grid(rows, columns)
    next_gen = start_grid(rows, columns)

    gen = 1
    for gen in range(1, generations + 1):
        if not move_grid(rows, columns, grid):
            break
        print_grid(rows, columns, current_gen, next_gen)
        current_gen, next_gen = next_gen, current_gen

    print_grid(rows, columns, current_gen, gen)

main(argv)

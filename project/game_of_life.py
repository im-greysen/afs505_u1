from sys import argv

def first_grid(grid, locations):

    for live in locations:
        i, j = live.split(':')
        grid[int(i)-1][int(j)-1] = 1

def print_grid(grid, rows, cols):
    for i in range(rows - 1):
        for j in range(cols - 1):
            if grid[i][j] == 1: print("X", end = "")
            if grid[i][j] == 0: print("-", end = "")
        print()
    print()

def active_grid(grid, rows, cols):

    next_grid = [[0] * cols for i in range(rows)]
    for i in range(rows - 1):
        for j in range(cols - 1):
            neighbor = int(grid[i - 1][j - 1]) + \
            int(grid[i][j - 1]) + int(grid[i + 1][j - 1]) + int(grid[i - 1][j]) + \
            int(grid[i + 1][j]) + int(grid[i - 1][j + 1]) + int(grid[i][j + 1]) + \
            int(grid[i + 1][j + 1])

            if grid[i][j] == 1 and neighbor < 2:
                next_grid[i][j] = 0
            elif grid[i][j] == 1 and (neighbor == 2 or neighbor == 3):
                next_grid[i][j] = 1
            elif grid[i][j] == 1 and neighbor > 3:
                next_grid[i][j] = 0
            elif grid[i][j] == 0 and neighbor == 3:
                next_grid[i][j] = 1

    return(next_grid)


def main(argv):

    script = argv[0]
    ticks = int(argv[1])
    locations = argv[2:]
    rows = 31
    cols = 81
    grid = [[0] * cols for i in range(rows)]
    tick = 0

    first_grid(grid, locations)
    print_grid(grid, rows, cols)

    while tick < ticks:
        grid = active_grid(grid, rows, cols)
        print_grid(grid, rows, cols)
        tick += 1

if __name__ == "__main__":
    main(argv)

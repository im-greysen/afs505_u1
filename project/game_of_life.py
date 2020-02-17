"""Conway's Game of Life Python Script.

.. module:: AFS505_U1 Project_01
    :platform: Windows
    :synopsis: This is a Python3 script for Conway's Game of Life, a cellular automation program that implements
    rules designed to mimic a cellular lifeform. Thi specific program achieves this goal by using a matrix with 30 rows
    and 80 columns. This zero player game will run for the user-specified amount of ticks, ticks in this case refers. to the
    number of generations

.. moduleauthor:: Greysen W. Danae greysen.danae@wsu.edu
.. modulereviewer: Nicole Rouleau nicole.rouleau@wsu.edu
"""


# reviewerscore: 100

from sys import argv

def first_grid(grid, locations):
    """Activates grid cells by converting 0s to 1s within the starting grid.

    :param locations: the locations of the cell index in each row and column
    :param grid: establishes the dimensions of the matrix
    :type locations: string
    :type grid: list

    :return: A 30x80 matrix that has all active cells representing values of 1
    :rtype: A 2400 element list with specified elements having a value of 1

    """

    for live in locations:
        i, j = live.split(':') # numbers in command line are split if there is a colon separation
        grid[int(i)-1][int(j)-1] = 1

def print_grid(grid, rows, cols):

    """Establishes a 30x80 matrix and converts elements with values of 0 to '-'
       and elements with values of 1 to 'X', simultaneously preserving numerical values.

    :param grid: gives the size of the matrix
    :param rows: an integer for the quantity of rows
    :param cols: an integer for the quantity of columns
    :type grid: string
    :type rows: int
    :type cols: int

    :return: a matrix of '-' & 'X' symbols specified by the command line inputs
    :rtype: a list of 2400 elements of either '-' or 'X' symbols
    """


    for i in range(rows - 1):
        for j in range(cols - 1):
            if grid[i][j] == 1: print("X", end = "")
            if grid[i][j] == 0: print("-", end = "")
        print() # prints the '-' and 'X' values
    print() # prints the 30x80 matrix

def active_grid(grid, rows, cols):

    """A new grid matrix is created with 0 for all elements followed by application
       of Conway's rules to activate cells and retuns the activated grid.

       :param grid: gives the size of the matrix
       :param rows: an integer for the quantity of rows
       :param cols: an integer for the quantity of columns
       :type grid: string
       :type rows: int
       :type cols: int

       :return: a grid matrix with '-' and 'X' characters specified in command line
       :rtype: a list of 2400 elements containing either '-' or 'X' characters
       """

    next_grid = [[0] * cols for i in range(rows)] # creates new null grid matrix
    for i in range(rows - 1):
        for j in range(cols - 1):
            neighbor = int(grid[i - 1][j - 1]) + \
            int(grid[i][j - 1]) + int(grid[i + 1][j - 1]) + int(grid[i - 1][j]) + \
            int(grid[i + 1][j]) + int(grid[i - 1][j + 1]) + int(grid[i][j + 1]) + \
            int(grid[i + 1][j + 1]) # takes the summation of the neighbors in the specified cell locations

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

    """Takes comand line inputs while reading the code and runs with the specified inputs.

    :param argv: the argument vector
    :type argv: a list

    :return: nothing
    :rtype: nothing
    """

    script = argv[0] # calls the specified script
    ticks = int(argv[1]) # the number of generation cycles
    locations = argv[2:] # the specified cells in the grid matrix to be activated
    rows = 31 # the number of rows in the grid matrix
    cols = 81 # the number of columns in the grid matrix
    grid = [[0] * cols for i in range(rows)] # establishes the null value grid matrix
    tick = 0 # the number of ticks run by the program

    first_grid(grid, locations)
    print_grid(grid, rows, cols)

    while tick < ticks:
        grid = active_grid(grid, rows, cols) # implements rules and presents the resulting changes
        print_grid(grid, rows, cols)
        tick += 1

if __name__ == "__main__":
    main(argv)

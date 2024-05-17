# This program uses functions to turn the '-' in the two-dimensional lists to a number that increases in count based on
# how many '#' are adjacent to it vertically, horizontally and diagonally.

# The first function counts the adjacent mines shown as a '#'
# The amount of rows and columns are identified by using len(minesweep). The [0] index has been used in the columns to
# identify only the columns
def count_adjacent_mines(minesweep):
    rows = len(minesweep)
    columns = len(minesweep[0])

    # An empty count list is created and nested for loops are used to detect and append new rows and columns
    count = []
    for row in range(rows):
        new_row = []
        for column in range(columns):
            new_row.append(0)
        count.append(new_row)

    # Nested for loops are created which checks the condition that if character is '#' it stays as '#'. If it isn't '#'
    # then the else: statement runs which calls the second function, count_adjacent
    for row in range(rows):
        for column in range(columns):
            if minesweep[row][column] == '#':
                count[row][column] = '#'
            else:
                count[row][column] = count_adjacent(minesweep, row, column)

    return count


# The second function, count_adjacent is called at the end of the first function and it increases the count based on
# how many adjacent '#s' there are
# The nested for loops check the rows and columns on the current row/column, previous row/column and upcoming row/column
def count_adjacent(minesweep, row, column):
    count = 0
    for x in range(row-1, row+2):
        for y in range(column-1, column+2):
            # The count of the position increases by 1 if all of the conditions in the if statement are met as it means
            # the position is adjacent to a mine '#'. The checks >= 0 and < len(minesweep) ensures the program does not
            # go out of range of the minesweep grid
            if (x >= 0 and x < len(minesweep) and y >= 0 and y < len(minesweep[0]) and
                    minesweep[x][y] == '#'):
                count += 1
    return count

# minesweep grid input to be converted to the desired output
minesweep = [["-", "-", "-", "#", "#"],
             ["-", "#", "-", "-", "-"],
             ["-", "-", "#", "-", "-"],
             ["-", "#", "#", "-", "-"],
             ["-", "-", "-", "-", "-"]]

# Nested for loop calls the count_adjacent_mines function, which calls the count_adjacent function and is printed on a
# new line as per the desired output
#result = count_adjacent_mines(minesweep)
#print(result)
for row in count_adjacent_mines(minesweep):
     for new_line in row:
         print(new_line, end=' ')
     print()


def count_adjacent_mines(grid):
    rows = len(grid)
    cols = len(grid[0])
    #result = [[0 for _ in range(cols)] for _ in range(rows)]
    result = []
    for row in range(rows):
        new_row = []
        for column in range(cols):
            new_row.append(0)
        result.append(new_row)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '#':
                result[i][j] = '#'
            else:
                result[i][j] = count_adjacent(grid, i, j)

    return result

def count_adjacent(grid, i, j):
    count = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if (x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and
                    grid[x][y] == '#'):
                count += 1
    return count

grid = [ ["-", "-", "-", "#", "#"],
["-", "#", "-", "-", "-"],
["-", "-", "#", "-", "-"],
["-", "#", "#", "-", "-"],
["-", "-", "-", "-", "-"] ]


for row in count_adjacent_mines(grid):
    for new_line in row:
        print(new_line, end=' ')
    print()

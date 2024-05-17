# Create a 2D list representing the game grid
grid = [  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0]
]

# Set the mine positions in the grid
grid[1][3] = 1
grid[3][1] = 1
grid[4][4] = 1

# Function to count the number of mines around a given position
def count_mines(grid, x, y):
  count = 0
  # Check the positions above, below, left, and right of the given position
  if x > 0 and grid[x - 1][y] == 1:
    count += 1
  if x < len(grid) - 1 and grid[x + 1][y] == 1:
    count += 1
  if y > 0 and grid[x][y - 1] == 1:
    count += 1
  if y < len(grid[0]) - 1 and grid[x][y + 1] == 1:
    count += 1
  return count

# Loop through each position in the grid
for x in range(len(grid)):
  for y in range(len(grid[0])):
    # If the position is a mine, print "X"
    if grid[x][y] == 1:
      print("X", end=" ")
    # If the position is not a mine, print the number of mines around it
    else:
      print(count_mines(grid, x, y), end=" ")
  print()

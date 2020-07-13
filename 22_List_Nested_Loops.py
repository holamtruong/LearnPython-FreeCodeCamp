number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid)  # => 2D array
print(number_grid[0])  # => row 1
print(number_grid[2][1])  # => row 2, col 1

# A nested loop is a loop inside a loop
for row in number_grid:
    for col in row:
        print(col)

# index of row, col
for row in number_grid:
    for col in row:
        print(number_grid.index(row), row.index(col))

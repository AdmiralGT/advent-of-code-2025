def is_accessible(grid, row, col):
    count = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dr, dc in directions:
    # Check adjacent positions (up, down, left, right)
        r, c = row + dr, col + dc
        if grid[r][c] == '@':
            count += 1
    return count < 4

with open("input.txt") as f:
    lines = f.readlines()

# Recreate the grid with padding
# Add a line of blanks at the top and bottom
line_length = len(lines[0].strip())
lines.insert(0, '.' * line_length)
lines.append('.' * line_length)

grid = []
# Add a dot at the start and end of each line
for line in lines:
    line = list("." + line.strip() + ".")
    grid.append(line)

accessible_rolls = 0
for row in range(1, len(grid) - 1):
    for col in range(1, len(grid[row]) - 1):
        if grid[row][col] == '.':
            continue

        if is_accessible(grid, row, col):
            accessible_rolls += 1

print(f"Total accessible rolls: {accessible_rolls}")
        



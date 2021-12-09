def get_score(basins):
    sizes = [len(basin) for basin in basins]
    sizes.sort()
    three_largest = sizes[-3:]
    product = 1
    for basin_size in three_largest:
        product *= basin_size
    return product

with open("input_day9.txt") as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]

length_x = len(lines[0])
length_y = len(lines)

def get_neighbors(point, visited):
    neighbors = []
    x = point[0]
    y = point[1]
    if x > 0 and x < length_x-1:
        neighbors.extend([(x+1, y), (x-1, y)])
    elif x == 0:
        neighbors.append((x+1, y))
    elif x == length_x-1:
        neighbors.append((x-1, y))
    if y > 0 and y < length_y-1:
        neighbors.extend([(x, y+1), (x, y-1)])
    elif y == 0:
        neighbors.append((x, y+1))
    elif y == length_y-1:
        neighbors.append((x, y-1))

    filtered = [point for point in neighbors if point not in visited]
    return filtered


# Basic idea, start from a point and build the basin based on all neighbors and neighbors and so on
# If no neighbors or all neighhbors are tops, break and move on
total_points = length_x * length_y
heights = {}
for row_index in range(0, length_y):
    for col_index in range(0, length_x):
        heights[(col_index, row_index)] = int(lines[row_index][col_index])

visited = set()
basins = []
# Start somewhere
neighbors = []
neighbors.append((0, 0))
curr_basin = set()

while True:
    curr_point = neighbors.pop(0)
    visited.add(curr_point)
    curr_height = heights[curr_point]

    if curr_height != 9:
        curr_basin.add(curr_point)
        # Extend without duplication
        neighbors.extend([neighbor for neighbor in get_neighbors(curr_point, visited) if neighbor not in neighbors])
    if len(neighbors) == 0:
        # Hack to add a new random point if we are now empty
        if len(curr_basin) > 0:
            basins.append(curr_basin)
        if len(visited) >= total_points:
            break
        neighbors.append((set(heights.keys()) - visited).pop())
        curr_basin = set()


print(get_score(basins))
class Node:
    def __init__(self, coordinates, parent=None, score=None):
        self.coordinates = coordinates
        self.parent = parent
        self.score = score

with open("test_day15.txt") as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]

length_x = len(lines[0])
length_y = len(lines)
total_points = length_x * length_y

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

risk_levels = {(x, y): int(lines[y][x]) for x in range(length_x) for y in range(length_y)}

visited = set()
tentative_risks = {(0, 0): {"risk_level": 0, "parent": None}}
curr_node = (0, 0)
target = (length_x-1, length_y-1)
# As long as there are neighbors to search, continue
while len(visited) < total_points:
    curr_neighbors = get_neighbors(curr_node, visited)
    # Find the neighhbor with the lowest score
    for neighbor in curr_neighbors:
        total_tent_risk_level = risk_levels[neighbor] + tentative_risks[curr_node]["risk_level"]
        try:
            if total_tent_risk_level < tentative_risks[neighbor]["risk_level"]:
                tentative_risks[neighbor] = {"risk_level": total_tent_risk_level, "parent": curr_node}
        except KeyError:
            tentative_risks[neighbor] = {"risk_level": total_tent_risk_level, "parent": curr_node}

    risk_levels_to_search = {neighbor: tentative_risks[neighbor]["risk_level"] for neighbor in curr_neighbors}
    curr_node = min(risk_levels_to_search, key=risk_levels_to_search.get)
    visited.add(curr_node)
    best_next_level = risk_levels_to_search[curr_node]
    if curr_node == target:
        break

print(tentative_risks[target]["risk_level"])
parent = tentative_risks[target]["parent"]
print(target, tentative_risks[target])
while parent:
    print(parent, tentative_risks[parent])
    parent = tentative_risks[parent]["parent"]
def get_points(line):
    split = line.split(" -> ")

    point0 = (int(split[0].split(",")[0]), int(split[0].split(",")[1]))
    point1 = (int(split[1].split(",")[0]), int(split[1].split(",")[1]))

    if point0[0] == point1[0]:
        y1 = min(point0[1], point1[1])
        y2 = max(point0[1], point1[1])
        return [(point0[0], y) for y in range(y1, y2+1)]  # Inclusive
    elif point0[1] == point1[1]:
        x1 = min(point0[0], point1[0])
        x2 = max(point0[0], point1[0])
        return [(x, point0[1]) for x in range(x1, x2+1)]  # Inclusive
    else:
        x_min = min(point0[0], point1[0])
        x_max = max(point0[0], point1[0])
        y_min = min(point0[1], point1[1])
        y_max = max(point0[1], point1[1])
        length = x_max - x_min
        if ((point0[0] < point1[0] and point0[1] < point1[1])
            or (point0[0] > point1[0] and point0[1] > point1[1])):
            return [(x_min + offset, y_min + offset) for offset in range(0, length+1)]
        elif ((point0[0] > point1[0] and point0[1] < point1[1])
            or (point0[0] < point1[0] and point0[1] > point1[1])):
            return [(x_min + offset, y_max - offset) for offset in range(0, length+1)]

with open("input_day5.txt") as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]

all_points = []
counts = {}
for line in lines:
    points = get_points(line)
    all_points.extend(points)

for point in all_points:
    try:
        counts[point] += 1
    except KeyError:
        counts[point] = 1

print(len([count for count in counts.values() if count >=2]))

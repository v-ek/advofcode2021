with open("input_day2.txt") as file:
    lines = file.readlines()
# x = horizontal, y = depth, z = aim
position = [0, 0, 0]
for line in lines:
    words = line.split(" ")
    command = words[0]
    distance = int(words[1])
    if command == "forward":
        position[0] += distance
        position[1] += distance * position[2]
    elif command == "down":
        position[2] += distance
    elif command == "up":
        position[2] -= distance
multiplied = position[0] * position[1]
print(multiplied)

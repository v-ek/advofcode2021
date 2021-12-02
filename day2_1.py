with open("input_day2.txt") as file:
    lines = file.readlines()
# x = horizontal, y = depth
position = [0, 0]
for line in lines:
    words = line.split(" ")
    command = words[0]
    distance = int(words[1])
    if command == "forward":
        position[0] += distance
    elif command == "down":
        position[1] += distance
    elif command == "up":
        position[1] -= distance
multiplied = position[0] * position[1]
print(multiplied)

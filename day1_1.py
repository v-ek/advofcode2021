with open("input_day1.txt") as file:
    lines = file.readlines()
num_increases = 0
prev_line = lines[0]
for line in lines[1:]:
    if int(line) > int(prev_line):
        num_increases += 1
    prev_line = line
print(num_increases)

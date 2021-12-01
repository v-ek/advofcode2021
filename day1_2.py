with open("input_day1.txt") as file:
    lines = file.readlines()
num_increases = 0
prev_sum = int(lines[0]) + int(lines[1]) + int(lines[2]) 
for index in range(3, len(lines)):
    curr_sum = int(lines[index-2]) + int(lines[index-1]) + int(lines[index])
    if curr_sum > prev_sum:
        num_increases += 1
    prev_sum = curr_sum
print(num_increases)

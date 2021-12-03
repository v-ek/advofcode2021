with open("input_day3.txt") as file:
    lines = file.readlines()
# Assume nice input
num_digits = len(lines[0].strip())
col_sums = [0] * num_digits
num_entries = len(lines)
most_comm = [None] * num_digits 
least_comm = [None] * num_digits
for line in lines:
    line = line.strip()
    for index in range(num_digits):
        col_sums[index] += int(line[index])

for index in range(num_digits):
    if col_sums[index] / num_entries > 0.5:
        most_comm[index] = 1
        least_comm[index] = 0
    else:
        most_comm[index] = 0
        least_comm[index] = 1

gamma_rate = int("".join([str(digit) for digit in most_comm]), 2)
epsilon_rate = int("".join([str(digit) for digit in least_comm]), 2)
power_consumption = gamma_rate * epsilon_rate

print(power_consumption)

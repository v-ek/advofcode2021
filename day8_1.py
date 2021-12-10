with open("input_day8.txt") as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]

# Logic, look at the part after the | and split on spaces, and merge everyting into one list
outputs = [sig_pattern for line in lines for sig_pattern in line.split("|")[1].strip().split(" ")]

number_of_simple_digits = 0
for output in outputs:
    if len(output) in (2, 4, 3, 7):
        number_of_simple_digits += 1

print(number_of_simple_digits)
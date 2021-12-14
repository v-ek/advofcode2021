with open("input_day14.txt") as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]

template = lines[0]
insertions = {}
single_counts = {}
double_counts = {}
evolutions = {}

# Build the counts
for char_index in range(len(template)-1):
    try:
        single_counts[template[char_index]] += 1
    except KeyError:
        single_counts[template[char_index]] = 1
    try:
        double_counts[template[char_index:char_index+2]] += 1
    except KeyError:
        double_counts[template[char_index:char_index+2]] = 1
try:
    single_counts[template[-1]] += 1
except KeyError:
    single_counts[template[-1]] = 1

print(single_counts)
print(double_counts)

# Insertion rules
for line in lines[2:]:
    split = line.split(" -> ")
    insertions[split[0]] = split[1]

# Idea, build the evolution rules from the translation dict
for key, value in insertions.items():
    tmp_dict = {}
    tmp_dict["single"] = {value: 1}
    if key[0] == value and key[1] == value:
        # One more pair
        tmp_dict["double"] = {value + value: 1}
    elif key == key[0] + value:
        tmp_dict["double"] = {value + key[1]: 1}
    elif key == value + key[1]:
        tmp_dict["double"] = {key[0] + value: 1}
    else:
        tmp_dict["double"] = {
            key: -1,
            key[0] + value: 1,
            value + key[1]: 1
        }
    evolutions[key] = tmp_dict

print(evolutions)

for iteration in range(40):
    # Store the previous count states
    new_single_counts = {}
    new_double_counts = {}
    for key, double_count in double_counts.items():
        count_rules = evolutions[key]
        for single_key, single_value in count_rules["single"].items():    
            try:
                new_single_counts[single_key] += single_value * double_count
            except KeyError:
                new_single_counts[single_key] = single_value * double_count
        for double_key, double_value in count_rules["double"].items():
            try:
                new_double_counts[double_key] += double_value * double_count
            except KeyError:
                new_double_counts[double_key] = double_value * double_count
    
    # Update the counts
    for key, value in new_single_counts.items():
        try:
            single_counts[key] += value
        except KeyError:
            single_counts[key] = value
    for key, value in new_double_counts.items():
        try:
            double_counts[key] += value
        except KeyError:
            double_counts[key] = value

freqs = list(single_counts.values())
print(max(freqs) - min(freqs))

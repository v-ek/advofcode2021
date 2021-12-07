def get_rating(entries, rating_type):
    if rating_type == "O2":
        tie_breaker = 1
    elif rating_type == "CO2":
        tie_breaker = 0
    num_digits = len(entries[0])
    # First pass, determine most common digit and create an index such that the list can be filtered
    col_sums = [0] * num_digits
    curr_list = entries.copy()
    num_entries = len(entries)
    criteria = [None] * num_digits 

    for digit_index in range(num_digits):
        for entry in curr_list:
            col_sums[digit_index] += int(entry[digit_index])
            if col_sums[digit_index] / num_entries > 0.5:
                # 1 for most common and 0 for least common
                criteria[digit_index] = 1 if rating_type == "O2" else 0
            elif col_sums[digit_index] / num_entries < 0.5:
                criteria[digit_index] = 0 if rating_type == "O2" else 1
            else:
                criteria[digit_index] = tie_breaker
        curr_list = [entry for entry in curr_list if int(entry[digit_index]) == criteria[digit_index]]
        num_entries = len(curr_list)
        if len(curr_list) == 1:
            break
    return int(curr_list[0], 2)

with open("input_day3.txt") as file:
    lines = file.readlines()
# Sanitise the input
lines = [line.strip() for line in lines]

o2_rating = get_rating(lines, 'O2')
co2_rating = get_rating(lines, 'CO2')

print(o2_rating * co2_rating)

with open("input_day14.txt") as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]

template = lines[0]
translations = {}
counts = {}
for line in lines[2:]:
    split = line.split(" -> ")
    translations[split[0]] = split[1]

# The zeroth iteration is the template
results = [template]

for iteration in range(10):
    prev_seq = results[-1]
    chars_out = []
     # Loop over the string all the way, correct with minus one to use positive shift
    for char_index in range(len(prev_seq)-1):
        # If pair matches, append the middle "here"
        try:
            to_match = prev_seq[char_index:char_index+2]
            to_insert = translations[to_match]
            chars_out.extend([prev_seq[char_index], to_insert])
        except KeyError:
            chars_out.extend([prev_seq[char_index]])
    # Adjust for the fact that the last char is not appended
    chars_out.append(prev_seq[-1])
    results.append("".join(chars_out))

# Make the counts
for char in results[-1]:
    try:
        counts[char] += 1
    except KeyError:
        counts[char] = 1

freqs = list(counts.values())
freqs.sort()
print(freqs[-1] - freqs[0])
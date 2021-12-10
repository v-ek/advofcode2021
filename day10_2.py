with open("input_day10.txt") as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]
valid_openers = "([{<"
valid_closers = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}

# Simply invert the dict above
open_to_close_map = {v: k for k, v in valid_closers.items()}

score_map = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

# Store open in a "Stack", if closing found, check if "legal"
scores = []
for line in lines:
    # Fresh start on each line
    open_parens = []
    for char in line:
        if char in valid_openers:
            open_parens.append(char)
        elif char in valid_closers.keys():
            if valid_closers[char] != open_parens[-1]:
                break  # Move on to the next line, as this line is corrupted
            elif valid_closers[char] == open_parens[-1]:
                open_parens.pop()
    # If iteration finished, check for non-closed parens
    else:
        if len(open_parens) > 0:
            closing_parens = ''.join(reversed(open_parens))
            total_score = 0
            for char in closing_parens:
                total_score *= 5
                total_score += score_map[char]
            scores.append(total_score)

scores.sort()
print(scores[int(len(scores) / 2)])
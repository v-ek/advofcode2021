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

illegal_points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

# Store open in a "Stack", if closing found, check if "legal"
syntax_error_score = 0
for line in lines:
    # Fresh start on each line
    open_parens = []
    for char in line:
        if char in valid_openers:
            open_parens.append(char)
        elif char in valid_closers.keys():
            if valid_closers[char] != open_parens[-1]:
                syntax_error_score += illegal_points[char]
                break  # Move on to the next line, as this line is corrupted
            elif valid_closers[char] == open_parens[-1]:
                open_parens.pop()

print(syntax_error_score)
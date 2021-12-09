with open("input_day9.txt") as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]

length_x = len(lines[0])
length_y = len(lines)
low_points = {}

for row_index in range(0, length_y):
    for col_index in range(0, length_x):
        # Flags to re-use
        first_row = True if row_index == 0 else False
        first_col = True if col_index == 0 else False
        # Index is off-by one due to 0-indexing
        last_row = True if row_index == length_y-1 else False
        last_col = True if col_index == length_x-1 else False
        curr_height = int(lines[row_index][col_index])

        if first_row:
            if first_col:
                if (curr_height < int(lines[row_index][col_index + 1])
                    and curr_height < int(lines[row_index + 1][col_index])):
                    low_points[(row_index, col_index)] = curr_height + 1
            elif last_col:
                if (curr_height < int(lines[row_index][col_index - 1])
                    and curr_height < int(lines[row_index + 1][col_index])):
                    low_points[(row_index, col_index)] = curr_height + 1
            else:
                if (curr_height < int(lines[row_index][col_index + 1])
                    and curr_height < int(lines[row_index + 1][col_index])
                    and curr_height < int(lines[row_index][col_index - 1])):
                    low_points[(row_index, col_index)] = curr_height + 1

        elif last_row:
            if first_col:
                if (curr_height < int(lines[row_index][col_index + 1])
                    and curr_height < int(lines[row_index - 1][col_index])):
                    low_points[(row_index, col_index)] = curr_height + 1
            elif last_col:
                if (curr_height < int(lines[row_index][col_index - 1])
                    and curr_height < int(lines[row_index - 1][col_index])):
                    low_points[(row_index, col_index)] = curr_height + 1
            else:
                if (curr_height < int(lines[row_index][col_index + 1])
                    and curr_height < int(lines[row_index - 1][col_index])
                    and curr_height < int(lines[row_index][col_index - 1])):
                    low_points[(row_index, col_index)] = curr_height + 1

        else:
            if first_col:
                if (curr_height < int(lines[row_index][col_index + 1])
                    and curr_height < int(lines[row_index + 1][col_index])
                    and curr_height < int(lines[row_index - 1][col_index])):
                    low_points[(row_index, col_index)] = curr_height + 1
            elif last_col:
                if (curr_height < int(lines[row_index][col_index - 1])
                    and curr_height < int(lines[row_index + 1][col_index])
                    and curr_height < int(lines[row_index - 1][col_index])):
                    low_points[(row_index, col_index)] = curr_height + 1
            else:
                if (curr_height < int(lines[row_index][col_index + 1])
                    and curr_height < int(lines[row_index + 1][col_index])
                    and curr_height < int(lines[row_index][col_index - 1])
                    and curr_height < int(lines[row_index - 1][col_index])):
                    low_points[(row_index, col_index)] = curr_height + 1

print(sum(low_points.values()))
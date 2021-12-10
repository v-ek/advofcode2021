with open("input_day6.txt") as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]
fish_states = [int(state) for state in lines[0].split(",")]
state_vector = [0] * 9  # (0,1,...,8)

# Create initial state
for state in fish_states:
    state_vector[state] += 1

for day in range(0, 80):
    prev_state_vector = state_vector.copy()
    state_vector[8] = prev_state_vector[0]
    state_vector[7] = prev_state_vector[8]
    state_vector[6] = prev_state_vector[7] + prev_state_vector[0]
    state_vector[5] = prev_state_vector[6]
    state_vector[4] = prev_state_vector[5]
    state_vector[3] = prev_state_vector[4]
    state_vector[2] = prev_state_vector[3]
    state_vector[1] = prev_state_vector[2]
    state_vector[0] = prev_state_vector[1]

print(sum(state_vector))
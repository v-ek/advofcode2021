def get_cost(distance):
    return sum(i for i in range(1, distance+1))

with open("input_day7.txt") as file:
    line = file.readline()
line = line.strip()

start_positions = [int(entry) for entry in line.split(",")]
min_pos = min(start_positions)
max_pos = max(start_positions)

positions = []
fuel_costs = []
# Just brute force it, it would probably be possible to do a cleverer search method
for pos in range(min_pos, max_pos+1):
    fuel_costs.append(sum(get_cost(abs(start_pos - pos)) for start_pos in start_positions))
    positions.append(pos)

cheapest_index = fuel_costs.index(min(fuel_costs))
cheapest_pos = positions[cheapest_index]
cheapest_fuel_cost = fuel_costs[cheapest_index]

print(cheapest_fuel_cost)

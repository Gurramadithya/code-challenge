import math

locations = [(0, 0), (2, 3), (5, 1), (6, 4), (1, 2)]
priorities = ['high', 'medium', 'high', 'low', 'medium']

priority_order = {'high': 0, 'medium': 1, 'low': 2}


sorted_locations = sorted(zip(locations, priorities), key=lambda x: priority_order[x[1]])


def calculate_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def calculate_total_distance(route):
    total_distance = 0
    for i in range(1, len(route)):
        total_distance += calculate_distance(route[i-1], route[i])
    return total_distance


sorted_route = [loc[0] for loc in sorted_locations]

total_distance = calculate_total_distance(sorted_route)

print("Optimized Route:", sorted_route)
print("Total Distance: {:.2f} units".format(total_distance))

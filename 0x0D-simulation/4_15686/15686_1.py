import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
arr = [[0] * n for _ in range(n)]
all_chicken_locations =[]
house_locations = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        arr[i][j] = line[j]
        if arr[i][j] == 2:
            all_chicken_locations.append([i,j])
        elif arr[i][j] == 1:
            house_locations.append([i, j])

min_total_distance = float('inf')
k = len(all_chicken_locations)

def get_total_distance(chosen_indices):
    total_distance = 0
    chosen_chickens = [all_chicken_locations[i] for i in chosen_indices]
    for house in house_locations:
        min_dist_to_chicken = float('inf')
        for chicken in chosen_chickens:
            dist = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            min_dist_to_chicken = min(min_dist_to_chicken, dist)
        total_distance += min_dist_to_chicken
    return total_distance

def solve(index, chosen_count, chosen_indices):
    global min_total_distance
    if chosen_count == m:
        distance = get_total_distance(chosen_indices)
        min_total_distance = min(min_total_distance, distance)
        return
    if index == k:
        return

    # Pruning: if it's impossible to choose 'm' even if we take all remaining
    if k - index < m - chosen_count:
        return

    # Option 1: Choose the chicken restaurant at index
    solve(index + 1, chosen_count + 1, chosen_indices + [index])

    # Option 2: Don't choose it
    solve(index + 1, chosen_count, chosen_indices)

solve(0, 0, [])
print(min_total_distance)
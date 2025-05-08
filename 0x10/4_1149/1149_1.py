import sys
input = sys.stdin.readline

n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
# cost = [[26, 40, 83], [49, 60, 57], [13, 89, 99]]
min_cost = float('inf')

def backtrack(house, prev_color, current_cost):
    global min_cost
    
    # 현재까지의 비용이 이미 최소 비용을 넘어선 경우 더 이상 탐색하지 않음 (가지치기)
    if current_cost >= min_cost: return
        
    # 모든 집을 다 칠한 경우
    if house == n:
        min_cost = min(min_cost, current_cost)
        return
    
    # 현재 집을 R, G, B로 칠하는 경우를 각각 시도
    for color in range(3):
        if house > 0 and color == prev_color: continue # 이전 집과 같은 색은 칠할 수 없음
        
        # 다음 집으로 재귀 호출
        backtrack(house + 1, color, current_cost + cost[house][color])

# 첫 번째 집부터 시작 (이전 집이 없으므로 -1로 초기화)
backtrack(0, -1, 0)

print(min_cost)
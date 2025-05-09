from itertools import combinations
import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
arr = [[0] * n for _ in range(n)]
chicken_lst =[]
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        arr[i][j] = line[j]
        if arr[i][j] == 2: chicken_lst.append([i,j])

# n, m = [5, 3]
# arr = [[0, 0, 1, 0, 0],
#     [0, 0, 2, 0, 1],
#     [0, 1, 2, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 2]]

# n x n 배열
# 0은 빈 칸, 1은 집, 2는 치킨집
# m은 치킨집이 남을 개수

all_coms = combinations(chicken_lst,m)

chicken_dis = float('inf') # 최소 치킨 거리
for com in all_coms:
    total_dis = 0 # 한 조합에 대한 최소 치킨 거리
    for i in range(n):
        for j in range(n):
            # 한 집에서 조합에 있는 치킨집까지의 거리
            if arr[i][j] == 1:
                dis = float('inf') 
                for ch in com:
                    # 치킨집과 집의 거리
                    dis = min(dis, abs(i-ch[0]) + abs(j-ch[1]))
                total_dis += dis
    # 최소 거리 구하기
    chicken_dis = min(chicken_dis, total_dis)
print(chicken_dis)
import sys
from collections import deque

input = sys.stdin.readline

k = int(input())
m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx_h = [1, -1, 2, -2, 2, -2, 1, -1]
dy_h = [2, 2, 1, 1, -1, -1, -2, -2]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = deque()
queue.append((0,0,0)) # (x,y, 말을 사용한 횟수)

# 3D distance: dist[horse_used][x][y]
dist = [[[-1] * m for _ in range(n)] for _ in range(k+1)]
dist[0][0][0] = 0

while queue:
    x, y, horse = queue.popleft()
    if x == n-1 and y == m-1: break
    # 1. 말 움직임
    if horse < k:
        for i in range(8):
            nx = x + dx_h[i]
            ny = y + dy_h[i]
            if nx<0 or ny<0 or nx>=n or ny>=m: continue
            if board[nx][ny] == 1: continue
            if dist[horse+1][nx][ny] == -1 and horse+1 <= k:
                dist[horse+1][nx][ny] = dist[horse][x][y] + 1
                queue.append((nx,ny,horse+1))

    # 2. 원숭이 움직임
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx<0 or ny<0 or nx>=n or ny>=m: continue
        if board[nx][ny] == 1: continue
        if dist[horse][nx][ny] == -1:
            dist[horse][nx][ny] = dist[horse][x][y] + 1
            queue.append((nx,ny,horse))

min_dist = float('inf')
for h in range(k + 1):
    if dist[h][n-1][m-1] != -1:
        min_dist = min(min_dist, dist[h][n-1][m-1])

if min_dist == float('inf'):
    print(-1)
else:
    print(min_dist)

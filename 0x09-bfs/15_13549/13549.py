import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

# dist[i] : i번째 위치까지 도달하는 데 걸리는 최소 시간
MAX_SIZE = 100001
dist = [-1] * MAX_SIZE
dist[n] = 0

queue = deque()
queue.append(n)

while queue:
    x = queue.popleft()
    if x == k: break
    # 1. 순간이동
    next = x*2
    if 0 <= next < MAX_SIZE and dist[next] == -1:
        dist[next] = dist[x]
        queue.appendleft(next)
    # 2. 걷기
    if x-1 >= 0 and dist[x-1] == -1:
        dist[x-1] = dist[x]+1
        queue.append(x-1)
    if x+1 < MAX_SIZE and dist[x+1] == -1:
        dist[x+1] = dist[x] +1
        queue.append(x+1)
print(dist[k])

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    # Read each row, split by space, convert to integers, and store as a list
    graph.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

num_pictures = 0  # 그림의 개수 (number of connected components)
max_area = 0      # 그림의 최대 넓이 (maximum area of a component)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 or visited[i][j]: continue

        # Found the start of a new picture (connected component of 1s)
        num_pictures += 1
        current_area = 0

        queue = deque([(i, j)])
        visited[i][j] = True

        # Perform BFS to find all connected cells in this picture
        while queue:
            x, y = queue.popleft()  # Get the next cell from the queue
            current_area += 1      # Increment the area for this picture

            # Explore the 4 neighboring cells
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx<0 or nx>=n or ny<0 or ny>=m: continue
                if graph[nx][ny] != 1 or visited[nx][ny]: continue
                visited[nx][ny] = True
                queue.append((nx, ny))

        max_area = max(max_area, current_area)

print(num_pictures)
print(max_area)
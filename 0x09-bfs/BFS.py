from collections import deque

def solution(maps):
    # 상우하좌 움직임 
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    queue = deque()
    queue.append([0,0]) # 시작점
    n = len(maps) # row 
    m = len(maps[0]) # col
    dist = [[0] * m for _ in range(n)]
    dist[0][0] = 1
    
    while queue:
        x, y = queue.popleft()
        # 상하좌우 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵 밖
            if nx<0 or ny<0 or nx>=n or ny>=m: continue
            # 벽이거나 이미 간 곳
            if maps[nx][ny] == 0 or dist[nx][ny] > 0: continue
            dist[nx][ny] = dist[x][y] + 1
            queue.append([nx,ny])
    
    answer = dist[n-1][m-1]
    if answer == 0: return -1
    return answer
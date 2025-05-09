import sys
import copy
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)] # n x m 행렬
cctv = [] # [(x,y, cctv)] = [(2,2,1)]
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        arr[i][j] = line[j]
        if line[j] != 0 and line[j] != 6: cctv.append((i, j, line[j]))

# 0위쪽, 1왼쪽, 2아래쪽, 3오른쪽
dx = [-1,0,1,0]
dy = [0,-1,0,1]

# cctv 1개 당 4가지 방향 존재. 즉, 깊이마다 4개의 자식노드가 존재
# 1개를 지날 때마다 새로운 맵이 생김 (deep copy)
# dfs를 이용하여 모든 경우를 탐색
min_cnt = n * m # 최소 0의 개수 (모두 0인 경우)
def func(k, cur_arr):
    global min_cnt
    # cctv 개수만큼 반복
    if k == len(cctv):
        cnt = 0 # 0 개수
        for d in range(n):
            for j in range(m):
                if cur_arr[d][j]==0: cnt += 1
        min_cnt = min(cnt, min_cnt)
        return

	# k번째 cctv 탐색
    x, y, c_num = cctv[k]

    # cctv 1대당 방향 4가지
    for d in range(4):
        # 방향마다 맵이 달라짐
        copyarr = copy.deepcopy(cur_arr)
        # cctv 번호마다 가는 방향이 다름
        if c_num == 1:
            copyarr = move(x,y, d, copyarr)
        elif c_num == 2:
            copyarr = move(x,y, d, copyarr)
            copyarr = move(x,y, d+2, copyarr)
        elif c_num == 3:
            copyarr = move(x,y, d, copyarr)
            copyarr = move(x,y, d+1, copyarr)
        elif c_num == 4:
            copyarr = move(x,y, d, copyarr)
            copyarr = move(x,y, d+1, copyarr)
            copyarr = move(x,y, d+2, copyarr)
        elif c_num == 5:
            copyarr = move(x,y, 0, copyarr)
            copyarr = move(x,y, 1, copyarr)
            copyarr = move(x,y, 2, copyarr)
            copyarr = move(x,y, 3, copyarr)
        func(k+1, copyarr)

# 실제 탐색하는 함수
def move(x,y,d,copyarr):
    d %= 4
    while True:
        x, y = x+dx[d], y+dy[d]
        if x<0 or y<0 or x>=n or y>=m: break
        if copyarr[x][y] == 0: copyarr[x][y] = 7 # 7은 방문
    return copyarr

func(0, arr)
print(min_cnt)
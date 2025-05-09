import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
sticker = []
arr = [[0] * m for _ in range(n)] # 노트북 화면 n x m
for _ in range(k):
    r, c = map(int, input().split())
    arr1 = [[0] * c for _ in range(r)]
    for i in range(r):
        line = list(map(int, input().split()))
        for j in range(c):
            arr1[i][j] = line[j]
    sticker.append(arr1)

# 스티커 배열
# sticker = [[[1, 0, 1], [1, 1, 1], [1, 0, 1]],
# [[1, 1, 1, 1, 1], [0, 0, 0, 1, 0]],
# [[1, 1, 1], [1, 0, 1]],
# [[1, 0, 0], [1, 1, 1], [1, 0, 0]]]

# 1. 일단 붙이기 시도 (맨 왼쪽 위)
#  붙이는 위치가 고정이라 카피본은 필요 없음
#  가장 위 -> 가장 왼쪽 순서로 시도
# 2. 안되면 90도 회전. 시계방향으로 총 4회 시도

# kn번째 스티커 붙이기
def func(kn):
    # 모든 스티커 시도 완료
    if kn == k:
        cnt = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 1: cnt += 1
        return cnt

    st = sticker[kn]
    r, c = len(st), len(st[0])
    # 1. (0,0) 부터 붙이기 시도
    for i in range(n-r+1):
        for j in range(m-c+1):
            if check(i,j, st): return func(kn+1)
	
	# 2. 못붙이면 회전해서 붙이기 시도
    # 총 3번 회전 가능
    for rd in range(1,4):
        rotated = rotate(st, rd)
        r, c = len(rotated), len(rotated[0])
        for i in range(n-r+1):
            for j in range(m-c+1):
                if check(i,j, rotated): return func(kn+1)

    # 3. 그래도 못붙이면 버리고 다음 스티커 시도
    return func(kn+1)

def check(x, y, st):
    global arr
    r, c = len(st), len(st[0])
    for i in range(r):
        for j in range(c):
            if st[i][j] == 1 and arr[x+i][y+j] == 1: return False
    # 붙이기 가능. 바로 arr 배열에 붙이기
    for i in range(r):
        for j in range(c):
            if st[i][j] == 1: arr[x+i][y+j] = 1
    return True

# 00 01 02
# 10 11 12
# 20 21 22
  
# 90도 회전
# 20 10 00
# 21 11 01
# 22 12 02

# B(00) -> A(20)
# B(01) -> A(10)
# B(02) -> A(00)
# B(10) -> A(21)
# B(11) -> A(11)
# B(12) -> A(01)
# B(x, y) -> A(3-1-y ,x)
  
def rotate(st, rd):
	# rd는 1,2,3 (90, 180, 270)
	# 90도 회전을 rd 수 만큼 수행
	if rd == 0: return st
	r, c = len(st), len(st[0])
	tmp = [[0] * r for _ in range(c)]
	for i in range(c):
		for j in range(r):
			tmp[i][j] = st[r-1-j][i]
	return rotate(tmp, rd-1)

print(func(0))
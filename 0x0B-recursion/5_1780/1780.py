import sys

input = sys.stdin.readline
n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))

# 개수를 담는 배열
# index로 접근하기 쉽게 배열함
# 0로만 채워진 종이, 1로만 채워진 종이, -1로만 채워진 종이,
result = [0]* 3

# map이 같은 수로 되어 있는 지 확인하는 함수
def is_equal(x,y,n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[x][y] != arr[i][j]:
                return False
    return True

# 0, 0에서 시작하는 길이가 n인 배열의 
def func(x, y, n):
    # 종이가 같은 수로 되어 있으면 종료
    if is_equal(x,y,n):
        result[arr[x][y]] += 1
        return
    
    new_n = n // 3
    for i in range(3):
        for j in range(3):
            func(x+i*new_n, y+j*new_n, new_n)

# n=9
func(0, 0, n)
print(result[-1])
print(result[0])
print(result[1])
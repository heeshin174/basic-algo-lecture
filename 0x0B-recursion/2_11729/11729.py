import math
n = int(input()) # 원판의 개수

# 재귀식: n번 원판을 기둥 a에서 기둥 b로 옮긴다.
def func(a, b, n):
	# n = 1일 때 a에서 b로 옮긴다.
	if n == 1:
		print(f"{a} {b}")
		return
	
	func(a, 6-a-b, n-1)
	print(f"{a} {b}")
	func (6-a-b, b, n-1)

# 일반항 2^k-1
print(int(math.pow(2, n) - 1))
# n번 원판을 1에서 3으로 옮기는 재귀 함수
func(1, 3, n)
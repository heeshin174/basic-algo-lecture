n, r, c = map(int, input().split())

# 2^n X 2^n 배열에서 (r, c)을 몇 번째로 방문했는 지 계산하는 함수
def func(n,r,c):
	if n == 0: return 0 
	# 한 변 길이의 절반
	half = 2 ** (n-1)
	if r<half and c<half: return func(n-1,r,c)
	elif r<half and c>=half: return half*half + func(n-1,r,c-half)
	elif r>=half and c<half: return 2*half*half + func(n-1,r-half,c)
	elif r>=half and c>=half: return 3*half*half + func(n-1,r-half,c-half)

print(func(n,r,c))
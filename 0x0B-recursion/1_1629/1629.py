# a, b, c
# a를 b번 곱한 후 c로 나눈 나머지 구하기
# a * a * a
def solution(a, b, c):
	# 효율적인 재귀: 분할 정복 (빠른 거듭제곱)
    def rec(n, b):
        if b == 0:
            return 1
        # b가 짝수인 경우
        if b % 2 == 0:
            half = rec(n, b // 2)
            return (half * half) % c
        # b가 홀수인 경우
        else:
            return (n * rec(n, b - 1)) % c
            
    return rec(a, b)

solution(10, 11, 12) # 4
# 10 * 10 * 10 ...을 (11번) 한 후 12로 나눈 나머지 (modular 12)
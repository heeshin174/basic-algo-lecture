n = int(input())

# dp[i] : i번째 계단을 도달하기 위한 최대값
# 300이 최대값이므로 305로 설정
dp = {}
score = {}

for i in range(1, n+1):
    score[i] = int(input())

# n이 1이거나 2일 때는 dp를 계산하지 않음
if n == 1:
    print(score[1])
    exit()
elif n == 2:
    print(score[1] + score[2])
    exit()

dp[1] = score[1]
dp[2] = dp[1] + score[2]
dp[3] = max(dp[1] + score[3], dp[2] + score[3])

for i in range(4, n+1):
    dp[i] = score[i] + max(dp[i-3] + score[i-1], dp[i-2])

print(dp[n])


'''
개선점: 딕셔너리로 선언해도 되지만, 이 경우 1,2,3, ... n까지의 값을 저장해야 하므로 리스트로 선언하는 것이 더 메모리 효율적이다.

dp = [0] * (n + 1)
score = [0]  # index 맞추기 위해 0 추가
for _ in range(n):
    score.append(int(input()))

- 시간 복잡도: O(N)
for 반복문 한 번 돌기 때문에 맞습니다.

- 공간 복잡도: O(N)
dp, score 둘 다 길이가 N이므로 총 2N이지만, 빅-오는 계수 무시하니까 O(N) 맞습니다.
'''
import sys
input = sys.stdin.readline

n = int(input())

score = []
for _ in range(n):
    score.append(list(map(int, input().split())))

dp = []
for i in range(1, n+1):
    dp.append([0] * i)

dp[0][0] = score[0][0]

for i in range(1, n):
    for j in range(0, i+1):
        if j == 0: dp[i][j] = dp[i-1][j] + score[i][j] # 맨 왼쪽 열은 위에서만 내려 옴
        elif j == i: dp[i][j] = dp[i-1][j-1] + score[i][j] # 맨 오른쪽 열은 대각선 위에서만 올라 옴
        else: dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + score[i][j]

print(max(dp[n-1])) 
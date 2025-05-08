import sys
input = sys.stdin.readline

n = int(input())

score = [[0] * 3 for _ in range(n+1)]
dp = [[0] * 3 for _ in range(n+1)]

for i in range(1, n+1):
    r, g, b = map(int, input().split())
    score[i][0] = r
    score[i][1] = g
    score[i][2] = b

dp[1][0] = score[1][0]
dp[1][1] = score[1][1]
dp[1][2] = score[1][2]

for i in range(2, n+1):
    dp[i][0] = score[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = score[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = score[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[n][0], dp[n][1], dp[n][2]))
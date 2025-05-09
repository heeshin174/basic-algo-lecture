n = int(input())

dp = [0] * (n+1)
dp[1] = 0
prev = {}

for i in range(2,n+1):
    dp[i] = dp[i-1]+1
    prev[i] = i - 1 # i는 i-1에서 왔다고 기록
    if i%2 == 0:
        if dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1
            prev[i] = i // 2 # i는 i//2에서 왔다고 기록
    if i%3 == 0:
        if dp[i // 3] + 1 < dp[i]:
            dp[i] = dp[i // 3] + 1
            prev[i] = i // 3 # i는 i//3에서 왔다고 기록

print(dp[n])

# 경로 역추적 및 출력
current = n
path = []
while current > 1:
    path.append(current)
    current = prev[current]
path.append(1)

# 경로를 역순으로 출력 (N -> ... -> 1 순서)
print(*path) # 리스트 요소를 공백으로 구분하여 출력
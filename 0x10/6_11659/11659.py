import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
print(nums)
prefix_sum = [0] * (n+1)
prefix_sum[1] = nums[0]

for i in range(1, n):
    prefix_sum[i+1] = prefix_sum[i] + nums[i]

print(prefix_sum)
for i in range(m):
    start, end = map(int, input().split())
    print(prefix_sum[end] - prefix_sum[start-1])

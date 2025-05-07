t = int(input())

dic = {}
dic[1] = 1 # (1)
dic[2] = 2 # (1,1), (2)
dic[3] = 4 # (1,1,1), (1,2), (2,1), (3)

for i in range(4,11): # 1<= n < 11
    dic[i] = dic[i-1] + dic[i-2] + dic[i-3]

for i in range(t):
    n = int(input())
    print(dic[n])
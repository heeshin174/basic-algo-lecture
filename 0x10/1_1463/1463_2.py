n = int(input())

dic = {}
dic[1] = 0

for i in range(2,n+1):
    dic[i] = dic[i-1]+1
    if i%2 == 0:
        dic[i] = min(dic[i],dic[i//2]+1)
    if i%3 == 0:
        dic[i] = min(dic[i],dic[i//3]+1)

print(dic[n])

'''
Dictionary를 이용하여 이전 숫자를 저장하는 풀이

시간복잡도: 1부터 n까지 한 번 반복하기 때문에 O(n)이다.

for time complexity, we want to look at the operations that contribute most significantly as n grows. The core of this code is the for loop: for i in range(2, n+1):. This loop iterates from i = 2 all the way up to n.

Inside the loop, we perform a few operations: dictionary access (dic[i-1], dic[i//2], dic[i//3]), addition, comparison (min), modulo (%), and assignment. For Python dictionaries, these operations (access, insertion, update) are typically average O(1) time complexity – meaning they take roughly constant time regardless of the size of the dictionary.

Since the loop runs n-1 times, and the work done inside the loop is essentially constant time on average, the total time taken is directly proportional to n. As n doubles, the execution time roughly doubles.

Therefore, the time complexity of this algorithm is O(n). It scales linearly with the input size n

공간복잡도: dic이 최대로 가질 수 있는 공간이 O(N)이다.

For space complexity, we look at the memory used by the data structures, particularly how that usage scales with the input n. The main data structure here is the dictionary dic.

We start by initializing dic[1]. Then, within the loop, we add an entry dic[i] for every number i from 2 up to n. By the time the loop finishes, the dictionary dic will contain entries for all integers from 1 to n.

This means the dictionary will store exactly n key-value pairs. Each pair takes up a certain amount of memory. Since the number of entries in the dictionary grows directly with n, the total memory consumed by the dictionary is proportional to n.

Other variables like n, i, etc., use a constant amount of space regardless of how large n is.

So, the dominant factor in memory usage is the dictionary. Thus, the space complexity of this algorithm is also O(n). It requires an amount of memory that grows linearly with the input size n."
'''

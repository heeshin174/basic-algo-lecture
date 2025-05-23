# [1로 만들기](https://www.acmicpc.net/problem/1463)

정수 X에 세 가지 연산 사용

1. X // 3 (X % 3 == 0)
2. X // 2 (X % 2 == 0)
3. X - 1

1 <= X <= 10^6 (1,000,000)

## BFS를 이용한 풀이

그래프로 생각할 수 있다.

맨 위에 아무 것도 선택안한 노드에서 총 세 가지 선택의 갈림길이 주어짐. 하나씩 전부 따져볼 수 있지만 **최솟값**을 구하는 문제이기 때문에 DFS보단 BFS로 너비 우선 탐색을 하다가 **최솟값**이 발견되면 그 이후의 탐색은 할 필요가 없다.

```
     미선택
   /   |   \
  1    2    3
/ | \
1 2 3 
...
```

예를 들어, 10을 5로 만드는 방법에는 크게 두 가지가 있습니다.

1. `-1` 연산을 다섯 번 적용해서
   ```
   10 → 9 → 8 → 7 → 6 → 5
   ```

2. `÷2` 연산을 한 번만 적용해서
   ```
   10 → 5
   ```

만약 방문 체크 없이 탐색을 진행하면, 첫 번째 방법을 택하여 5에 도달하면, 이미 `÷2` 연산을 한 번만 적용해서 계속 자식 노드를 만들고 있던 연산을 중복으로 하게 된다.

따라서 한 번 처리한 숫자는 `visited` 배열로 표시하여, 이미 방문한 상태는 다시 큐에 넣지 않도록 하는 것이 효율적입니다.

## Dictionary를 이용한 풀이

1부터 n까지 최소 연산 횟수를 저장하는 dictionary를 이용한다. 

1부터 시작해 1만큼 증가시켜 n까지의 최소 연산 횟수를 전부 저장한다.

`dic = {1: 0, 2: 1, 3: 2, ...}`

`dic[1] = 0`은 1이 1이 되는 데 필요한 최소 연산 횟수가 0임을 의미한다.
`dic[2] = 1`은 2가 1이 되는 데 필요한 최소 연산 횟수가 1임을 의미한다.

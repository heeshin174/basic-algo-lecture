from collections import deque

n = int(input())
visited = [False] * (n + 1)

q = deque()
q.append((n, 0))
visited[n] = True  # 시작 상태 방문 처리

while q:
    cur, cnt = q.popleft()
    if cur == 1:
        print(cnt)
        break

    # 1) 3으로 나누어 떨어질 때
    if cur % 3 == 0:
        nxt = cur // 3
        if not visited[nxt]:
            visited[nxt] = True
            q.append((nxt, cnt + 1))

    # 2) 2로 나누어 떨어질 때
    if cur % 2 == 0:
        nxt = cur // 2
        if not visited[nxt]:
            visited[nxt] = True
            q.append((nxt, cnt + 1))

    # 3) 1을 빼는 연산
    nxt = cur - 1
    if not visited[nxt]:
        visited[nxt] = True
        q.append((nxt, cnt + 1))

'''
1463.py에서 방문 배열을 추가해 중복 방문을 방지한 풀이

이미 방문한 곳을 늦게 방문하면 이미 그 숫자는 더 적은 숫자로 방문할 확율이 있는 것이다. 그럼으로 다시 방문할 필요가 없기 때문에
visited 배열을 이용해서 이미 방문한 곳을 다시 방문하지 않도록 함.

Q. 시간복잡도: O(N)

우리가 탐색하는 숫자는 1부터 n까지, 최대 N개뿐입니다. 방문 배열을 써서 한 번 처리한 숫자는 다시 보지 않으므로, 큐에 들어가는 상태는 결코 n을 넘지 않습니다.

한 상태당 상수번 작업

큐에서 꺼내기(popleft)와 큐에 삽입(append)은 모두 O(1)
나머지 연산들(%3, %2, -1 연산, 방문 여부 체크)도 모두 O(1)
자식 상태 생성 및 enqueuing은 최대 세 번 발생하므로, **상수 c번**의 작업이 각 상태에 대해 실행됩니다.

총 연산량

상태 개수 N × 상태당 상수 작업 c → c×N번
따라서 빅오 표기법으로는 O(N) 이 됩니다.

이처럼 방문 배열 덕분에 각 숫자를 한 번만 처리하고, 처리할 때마다 하는 연산이 모두 상수 시간에 끝나므로 전체 탐색은 O(N) 시간이 든다.

Q. 공간복잡도: O(N)

두 가지 자료구조를 쓰는데, 둘 다 최악의 경우 N만큼 크기까지 커질 수 있기 때문입니다.

1. O(n)크기가 n + 1인 visited 배열
입력값 n에 대해 1부터 n까지 숫자의 방문 여부를 기록하는 boolean 배열을 만듭니다. 배열 길이가 n+1이므로 O(N) 공간이 필요합니다.

2. 큐(deque)
BFS를 위해 상태(숫자)와 연산 횟수 정보를 담은 튜플을 큐에 넣고 꺼내며 탐색합니다. 최악의 시나리오에서는 아직 처리되지 않은 모든 숫자(1부터 n)가 한꺼번에 큐에 남아 있을 수 있으므로, 큐도 O(N) 공간을 사용합니다.
따라서 두 구조를 합치면 여전히 O(N)+O(N)=O(N) 이고, 상수항이나 저차항은 무시하기 때문에 공간 복잡도는 O(N) 이다.
'''

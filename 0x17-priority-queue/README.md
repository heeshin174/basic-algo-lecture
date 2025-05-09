# [Priority Queue](../workbook/0x17.md)

우선순위 큐(Priority Queue)는 일반적인 큐(Queue)와 달리, **가장 먼저 들어온 데이터가 아닌, 우선순위가 가장 높은 데이터가 먼저 나오는 자료구조**입니다.

주로 힙(Heap)을 기반으로 구현되며, **최대 힙(max-heap)** 또는 **최소 힙(min-heap)** 형태로 사용됩니다.

## 주요 연산과 시간 복잡도

| 연산                                  | 설명                                                                                                                | 시간 복잡도            |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------- |
| **삽입 (Insert)**                     | 우선순위 큐에 새로운 요소를 추가합니다. 내부적으로 힙에 값을 추가하고, 힙 속성을 유지하기 위해 \*\*위로 올라가는 연산 (heapify-up)\*\*이 수행됩니다.                    | **O(log n)**      |
| **삭제 (Delete / Pop)**               | 가장 높은 우선순위를 가진 요소를 제거합니다. 일반적으로 루트 노드(최댓값 또는 최솟값)를 제거한 뒤, 마지막 노드를 루트로 올리고 \*\*아래로 내려가는 정렬(heapify-down)\*\*을 합니다. | **O(log n)**      |
| **우선순위 수정 (Decrease/Increase Key)** | 특정 요소의 우선순위를 변경합니다. 변경된 값이 클 경우에는 **heapify-up**, 작을 경우에는 **heapify-down**을 수행해 힙을 유지합니다.                         | **O(log n)** (최악) |

> **참고**: 일반 리스트로 구현한 우선순위 큐는 삽입 O(1), 삭제 O(n)이지만, 힙을 쓰면 모든 연산이 O(log n)으로 개선됩니다.

## 응용 분야

* 다익스트라 알고리즘 (최단 경로)
* A\* 알고리즘 (경로 탐색)
* 작업 스케줄링
* 실시간 이벤트 처리 시스템

## 요약

우선순위 큐는 데이터의 중요도에 따라 처리 순서를 정해야 하는 문제에서 매우 유용합니다. 일반적으로 힙(Heap) 자료구조를 기반으로 하며, 삽입, 삭제, 수정 모두 O(log n)의 시간 복잡도를 가집니다.

## Python에서 우선순위 큐

Python의 `heapq` 모듈을 활용한 **우선순위 큐 예제 코드**입니다.

기본적으로 `heapq`는 **최소 힙(min-heap)** 구조를 제공합니다. 즉, 항상 가장 작은 값이 먼저 나옵니다.

### 최소 힙 예제 (기본 사용)

```python
import heapq

pq = []  # 우선순위 큐 (빈 리스트)

# 값 삽입
heapq.heappush(pq, 5)
heapq.heappush(pq, 2)
heapq.heappush(pq, 8)
heapq.heappush(pq, 1)

# 값 꺼내기 (가장 작은 값부터)
while pq:
    print(heapq.heappop(pq), end=' ')  # 출력: 1 2 5 8
```

### 최대 힙 구현 (음수 활용)

Python의 `heapq`는 최대 힙을 직접 지원하지 않지만, **음수 값을 넣어 최소 힙처럼 동작하게 할 수 있습니다**.

```python
import heapq

pq = []

# 최대 힙처럼 사용: 음수로 넣고, 꺼낼 때 다시 음수로 돌림
heapq.heappush(pq, -5)
heapq.heappush(pq, -2)
heapq.heappush(pq, -8)
heapq.heappush(pq, -1)

while pq:
    print(-heapq.heappop(pq), end=' ')  # 출력: 8 5 2 1
```

### 우선순위와 값 함께 사용하기 (튜플 활용)

보통 실제 문제에서는 (우선순위, 값)의 형태로 다룹니다.

```python
import heapq

pq = []
heapq.heappush(pq, (2, "apple"))
heapq.heappush(pq, (1, "banana"))
heapq.heappush(pq, (3, "cherry"))

while pq:
    priority, value = heapq.heappop(pq)
    print(priority, value)
# 출력:
# 1 banana
# 2 apple
# 3 cherry
```

### 방법 1: 우선순위 수정 대신 새 항목을 삽입하고, 무효화 처리

Python의 `heapq`는 기본적으로 **우선순위 수정(Decrease Key)** 기능을 직접 제공하지 않습니다. 하지만 보통 아래 방법 중 하나로 구현합니다:

```python
import heapq

# (우선순위, 값)
pq = []
entry_finder = {}  # 실제 값 -> [우선순위, 값] 형태의 참조 저장
REMOVED = '<removed>'  # 삭제된 항목 표시용 마커

def add_task(task, priority):
    if task in entry_finder:
        remove_task(task)
    entry = [priority, task]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)

def remove_task(task):
    entry = entry_finder.pop(task)
    entry[1] = REMOVED  # 값 무효화

def pop_task():
    while pq:
        priority, task = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return priority, task
    raise KeyError('pop from an empty priority queue')

# 초기 삽입
add_task('A', 5)
add_task('B', 3)
add_task('C', 4)

# B의 우선순위 낮추기 (3 → 1)
add_task('B', 1)

# 꺼내기
while True:
    try:
        print(pop_task())
    except KeyError:
        break
# (1, 'B')
# (4, 'C')
# (5, 'A')
```

**왜 직접 수정하지 않고 새로 추가하나요?**

`heapq`는 내부에서 요소의 위치(index)를 모르기 때문에, 특정 요소의 우선순위를 직접 변경할 수 없습니다. 그래서 일반적으로는:

* **기존 요소는 무효화 처리** (`REMOVED`)
* **새로운 우선순위로 다시 삽입**

이런 방식으로 우선순위 수정을 구현합니다. 성능은 여전히 `O(log n)`이 유지됩니다.

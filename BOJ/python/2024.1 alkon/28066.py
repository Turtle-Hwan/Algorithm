# 28066 타노스는 요세푸스가 밉다 실2 / 알콘 4월 모의대회 div.2
'''
큐에 넣어놓고, 큐를 돌면서 제거할 것은 제거하고 다시 넣을 것은 뒤에 넣어주면 된다. => 시간 초과로 덱으로 변경

왜 덱이 빠른가? queue는 멀티스레딩 환경을 지원하기 위해 blocking을 wait 하거나 lock 같은 걸 거는 것 같다..
참고 : https://programming119.tistory.com/184
'''
from collections import deque

N, K = map(int, input().split())

N_deque = deque(range(1, N+1))

while (len(N_deque) >= K):
  N_deque.append(N_deque.popleft())
  for _ in range(K - 1):
    N_deque.popleft()

print(N_deque.popleft())
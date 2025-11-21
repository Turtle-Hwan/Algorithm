#I번 - 민들레 - 비트마스킹

import sys
input = sys.stdin.readline

N = int(input())

mindlele = 1

for i in range(N):
  c = input().split()
  if c[0] == 'Q':
    answer.append(len(mindlele))
  elif c[0] == 'C':
    if int(c[1]) not in mindlele:
      mindlele.add(int(c[1]))
  elif c[0] == 'R':
    n_min = set()
    for i in mindlele:
      n_min.add(i + 1)
    mindlele.update(n_min)
  elif c[0] == 'L':
    n_min = set()
    for i in mindlele:
      n_min.add(i - 1)
    mindlele.update(n_min)

[print(x) for x in answer]
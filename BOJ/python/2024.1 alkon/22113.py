# 22113 창영이와 버스 브1 / 알콘 4월 모의대회 div.2

N, M = map(int, input().split())
M_list = list(map(int, input().split()))
N_cost_list = list()

for i in range(N):
  N_cost_list.append(list(map(int, input().split())))

total_cost = 0
now_bus = 0
for m in M_list:
  if now_bus != 0:
    total_cost += N_cost_list[now_bus-1][m-1]
  now_bus = m

print(total_cost)
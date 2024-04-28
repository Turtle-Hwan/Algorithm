# 28138 재밌는 나머지 연산 실3 / 알콘 4월 모의대회 div.2

N, R = map(int, input().split())

sum_m = 0
if (N - R) <= R:
  print(sum_m)
else:
  n = N - R
  x = 1
  while (x <= n / x):
    if n / x == n // x:
      if x > R:
        sum_m += x
      if n // x > R and x != n // x:
        sum_m += n // x
    x += 1
  print(sum_m)

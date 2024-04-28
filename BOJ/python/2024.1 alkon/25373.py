# 25373 벼락치기 브2 / 알콘 4월 모의대회 div.2

N = int(input())

# 6 5 4 3 2 1 0  / 7n + 21
if N > 15:
  if (N - 21) % 7 != 0:
    print((N - 21) // 7 + 7)
  else:
    print((N - 21) // 7 + 6)
elif N > 10 and N <= 15:
  print(5)
elif N > 6 and N <= 10:
  print(4)
elif N > 3 and N <= 6:
  print(3)
elif N > 1 and N <= 3:
  print(2) 
elif N == 1:
  print(1)

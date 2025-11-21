# 30802.py

N = input()
TShirts = list(map(int, input().split()))
T, P = map(int, input().split())

## TShirts 순회하면서 묶음 단위로
TShirt_total = 0
for T_num in TShirts:
  TShirt_total += T_num // T
  TShirt_total += 0 if T_num % T == 0 else 1
  

print(TShirt_total)

## 펜은 N 이하 P * x개 + y개
print(int(N) // P, int(N) % P)


# 3711 학번 실5 / 알콘 4월 모의대회 div.2

def stu_m():
  G = int(input())
  student_list = list()
  for _ in range(G):
    student_list.append(int(input()))
  if G == 1:
    return 1
  
  remainder_list = list()
  divider = 1
  while len(remainder_list) != G:
    for i in student_list:
      if i % divider in remainder_list:
        divider += 1
        remainder_list.clear()
        break
      remainder_list.append(i % divider)
  return divider


N = int(input())
answer = list()

for _ in range(N):
  answer.append(stu_m())

[print(x) for x in answer]
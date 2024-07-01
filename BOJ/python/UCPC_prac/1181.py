# 단어 정렬

N = int(input())

word_list = list()
for i in range(N):
  word_list.append(input())

print(*sorted(set(word_list), key=lambda x:(len(x), x)))

# lambda == 화살표 함수, lambda input: output
# 이때 output 튜플로 주면 앞에서부터 정렬 우선순위가 된다.
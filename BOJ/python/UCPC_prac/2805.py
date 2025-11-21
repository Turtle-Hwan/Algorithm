# 나무 자르기 / 매개변수 탐색 / 이분탐색

def tree_len(h, tree_list):
  home_tree_len = 0
  for l in tree_list:
    if l - h > 0:
      home_tree_len += l - h
  return home_tree_len

# 
N, M = map(int, input().split())
tree_list = list(map(int, input().split()))

max_tree = max(tree_list)

right = max_tree
left = 0
h = (right - left) // 2
while right > left:
  #print(h, tree_len(h, tree_list), right, left)
  if tree_len(h, tree_list) > M:
    left = h + 1
    h += (right - left) // 2
  elif tree_len(h, tree_list) < M:
    right = h - 1
    h -= (right - left) // 2
  else:
    break

print(h)

'''
절단기의 높이 H 일때, 최댓값, 최솟값 절반으로 H 잡음.
잘린 나무가 많으면 H up
잘린 나무가 적으면 H down

//
이분탐색
값. -> 결과
결과에 따라 값 조정

//
upper bound : value보다 큰 값을 가지는 첫 iterator
lower bound : value보다 크거나 같은 값을 가지는 첫 iterator

ex) [1, 3, 5, 5, 5, 7]
lower : 처음 5
upper : 7

=> if value >= 5: 이동 lower
if value > 5: 

//


'''
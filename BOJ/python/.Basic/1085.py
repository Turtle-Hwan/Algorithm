#1085번 직사각형에서 탈출

#직사각형 각 변까지의 거리 중 최솟값

x, y, w, h = map(int, input().split())

distance = [x, y, w-x, h-y]

print(min(distance))

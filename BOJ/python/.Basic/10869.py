#10869번 사칙연산

a, b = input().split()

A = int(a)
B = int(b)

print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)

'''
왜 int(input().split()) 은 안돼서 따로 int() 해줘야 하는가?
'''

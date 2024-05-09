N = list(map(int, input().split()))
test = N[0] #テストの回数
student = N[1] #学生数

A = [[0 for _ in range(test)] for _ in range(student)]
for i in range(student):
    A[i] = list(map(int, input().split()))

point=[0 for _ in range(student)]
max_temp=0

for i in range(test):
    for j in range(student):
        if max_temp < A[j][i]:
            max_temp = A[j][i]
            index=j
    point[index] += 1
    max_temp = 0
    index = 0

for i in range(student):
    if point[i]==max(point):
        print(i+1, max(point))
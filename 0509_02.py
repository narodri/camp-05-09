test, student = map(int, input().split())
point = [0] * student

A = [[0 for _ in range(test)] for _ in range(student)]
for x in range(student):   
    A[x] = list(map(int, input().split()))

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
